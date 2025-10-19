"""
Command-line tool for checking eCourts listings.
"""
import argparse
import datetime
import os

from .ecourts_api import EcourtsAPI, EcourtsAPIError
from .downloader import download_file
from .utils import dates_for_when, save_json
from .config import OUTPUT_DIR


def build_case_no(case_type, number, year):
    return f"{case_type} {number}/{year}" if case_type and number and year else None


def find_case_in_causelist(causelist_json, cnr=None, case_no=None):
    # Generic search that works for many API shapes. You will likely need to adapt this
    # to the exact JSON fields your chosen API delivers.
    hits = []
    # Try several keys where cases may be held
    candidates = []
    if isinstance(causelist_json, dict):
        # common patterns: {'cases': [...]} or {'data': {'cases': [...]}}
        if "cases" in causelist_json:
            candidates = causelist_json.get("cases", [])
        elif "data" in causelist_json and isinstance(causelist_json["data"], dict):
            candidates = causelist_json["data"].get("cases", [])
        else:
            # last resort: look for list values
            for v in causelist_json.values():
                if isinstance(v, list):
                    candidates = v
                    break
    elif isinstance(causelist_json, list):
        candidates = causelist_json

    for item in candidates:
        # try multiple keys
        item_cnr = item.get("cnr") or item.get("CNR") or item.get("cnr_no")
        item_case_no = item.get("case_no") or item.get("case_number") or item.get("caseno") or item.get("caseId")
        if cnr and item_cnr and cnr.strip().lower() == str(item_cnr).strip().lower():
            hits.append(item)
        elif case_no and item_case_no and case_no.strip().lower() == str(item_case_no).strip().lower():
            hits.append(item)
    return hits


def main():
    p = argparse.ArgumentParser(description="eCourts listing checker CLI")
    p.add_argument("--cnr", help="Full CNR number")
    p.add_argument("--case-type", help="Case type (if not using CNR)")
    p.add_argument("--number", help="Case number")
    p.add_argument("--year", help="Year of case")
    p.add_argument("--when", choices=["today", "tomorrow", "both"], default="today")
    p.add_argument("--causelist", action="store_true", help="Download full cause list for the specified court/date")
    p.add_argument("--state", help="State name (if API requires it)")
    p.add_argument("--district", help="District name (if API requires it)")
    p.add_argument("--court-id", help="Court identifier (required for cause list fetching)")
    p.add_argument("--download-pdf", action="store_true", help="Download PDF if a PDF link is found")
    p.add_argument("--offline", action="store_true", default=True, help="Use offline mode with sample data files (default: True)")
    p.add_argument("--online", action="store_true", help="Use online mode to connect to real API")

    args = p.parse_args()

    # If --online is explicitly set, disable offline mode
    if args.online:
        args.offline = False
    
    api = EcourtsAPI(offline_mode=args.offline)
    dates = dates_for_when(args.when)
    query_case_no = build_case_no(args.case_type, args.number, args.year)

    summary = {"query": vars(args), "found": False, "listings": []}

    for d in dates:
        date_str = d.isoformat()
        print(f"Checking date: {date_str}")
        if not args.court_id:
            print("Warning: --court-id is recommended for accurate cause list retrieval")

        try:
            causelist = api.get_cause_list(court_id=args.court_id or "", date_str=date_str, state=args.state, district=args.district)
        except EcourtsAPIError as e:
            print("Failed to fetch cause list:", e)
            causelist = None

        if causelist:
            if args.causelist:
                fname = f"causelist_{args.court_id}_{date_str}.json"
                save_path = save_json(fname, causelist)
                print("Saved cause list to", save_path)

            hits = find_case_in_causelist(causelist, cnr=args.cnr, case_no=query_case_no)
            if not hits:
                print("No matching case found in the cause list for this date.")
            for h in hits:
                entry = {
                    "date": date_str,
                    "court_name": (causelist.get("court_name") if isinstance(causelist, dict) else None) or args.court_id,
                    "serial_no": h.get("serial_no") or h.get("sl_no") or h.get("sr_no"),
                    "case": h,
                }
                # if PDF link present
                pdf_link = h.get("pdf_url") or h.get("notice_pdf") or h.get("pdf")
                if pdf_link and args.download_pdf:
                    try:
                        local = download_file(pdf_link)
                        entry["pdf_local"] = local
                        print("Downloaded PDF to", local)
                    except Exception as e:
                        print("Failed to download pdf:", e)
                summary["listings"].append(entry)
                summary["found"] = True

    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    # Sanitize filename by replacing invalid characters
    case_identifier = (args.cnr or query_case_no or 'query').replace('/', '_').replace('\\', '_').replace(' ', '_')
    outname = f"query_result_{case_identifier}_{timestamp}.json"
    outpath = save_json(outname, summary)
    print("Saved query summary to", outpath)
    if summary["found"]:
        print("Case listed. See details in the saved JSON.")
    else:
        print("Case not listed on the requested date(s).")


if __name__ == "__main__":
    main()
