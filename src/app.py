"""
Simple Flask API that exposes a /check endpoint to run the same check as the CLI.
POST or GET parameters: cnr OR case_type, number, year; when (today/tomorrow/both); court_id; state; district
"""
from flask import Flask, request, jsonify
from .ecourts_api import EcourtsAPI, EcourtsAPIError
from .utils import dates_for_when
from .cli import build_case_no, find_case_in_causelist

app = Flask(__name__)
api = EcourtsAPI()


@app.route('/check', methods=['GET', 'POST'])
def check():
    payload = request.json or request.values
    cnr = payload.get('cnr')
    case_type = payload.get('case_type')
    number = payload.get('number')
    year = payload.get('year')
    when = payload.get('when') or 'today'
    court_id = payload.get('court_id')
    state = payload.get('state')
    district = payload.get('district')

    case_no = build_case_no(case_type, number, year)
    results = {"found": False, "listings": []}

    for d in dates_for_when(when):
        date_str = d.isoformat()
        try:
            causelist = api.get_cause_list(court_id=court_id or '', date_str=date_str, state=state, district=district)
        except EcourtsAPIError as e:
            return jsonify({"error": str(e)}), 500
        hits = find_case_in_causelist(causelist, cnr=cnr, case_no=case_no)
        for h in hits:
            entry = {"date": date_str, "court": causelist.get('court_name') if isinstance(causelist, dict) else court_id, "case": h}
            results['listings'].append(entry)
            results['found'] = True

    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
