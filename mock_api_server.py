"""
Mock eCourts API Server for Testing
Run this server first, then run your CLI tool with API_BASE pointing to http://localhost:5001
"""
from flask import Flask, jsonify, request
from datetime import date, timedelta

app = Flask(__name__)

# Sample cause list data
SAMPLE_CAUSE_LISTS = {
    "101": {
        "court_name": "District Court - Kadapa",
        "court_id": "101",
        "cases": [
            {
                "cnr": "ABCD1234567890123",
                "case_no": "CIV 123/2024",
                "case_type": "Civil",
                "serial_no": "15",
                "sl_no": "15",
                "party_names": "Ram Kumar vs Shyam Singh",
                "advocate": "Adv. Rajesh Sharma",
                "purpose": "Final Arguments",
                "pdf_url": "http://localhost:5001/pdf/case_123.pdf"
            },
            {
                "cnr": "WXYZ9876543210987",
                "case_no": "CRLP 456/2023",
                "case_type": "Criminal",
                "serial_no": "22",
                "sl_no": "22",
                "party_names": "State vs Mohan Lal",
                "advocate": "Adv. Priya Verma",
                "purpose": "Hearing",
                "pdf_url": "http://localhost:5001/pdf/case_456.pdf"
            },
            {
                "cnr": "PQRS5555666677778",
                "case_no": "CIV 789/2024",
                "case_type": "Civil",
                "serial_no": "8",
                "sl_no": "8",
                "party_names": "Lakshmi Devi vs Municipal Corporation",
                "advocate": "Adv. Suresh Kumar",
                "purpose": "Evidence",
                "pdf_url": "http://localhost:5001/pdf/case_789.pdf"
            }
        ]
    },
    "102": {
        "court_name": "High Court - Andhra Pradesh",
        "court_id": "102",
        "cases": [
            {
                "cnr": "HCAP1111222233334",
                "case_no": "WP 1001/2024",
                "case_type": "Writ Petition",
                "serial_no": "5",
                "sl_no": "5",
                "party_names": "Vijay Enterprises vs State of AP",
                "advocate": "Sr. Adv. Ramesh Babu",
                "purpose": "Final Hearing",
                "pdf_url": "http://localhost:5001/pdf/case_1001.pdf"
            }
        ]
    }
}


@app.route('/cnr/<cnr>', methods=['GET'])
def search_by_cnr(cnr):
    """Search case by CNR number"""
    for court_id, court_data in SAMPLE_CAUSE_LISTS.items():
        for case in court_data["cases"]:
            if case["cnr"].lower() == cnr.lower():
                return jsonify({
                    "success": True,
                    "case": case,
                    "court": court_data["court_name"]
                })
    return jsonify({"success": False, "message": "Case not found"}), 404


@app.route('/cause-list', methods=['GET'])
def get_cause_list():
    """Get cause list for a court and date"""
    court_id = request.args.get('court_id', '101')
    date_str = request.args.get('date')
    state = request.args.get('state')
    district = request.args.get('district')
    
    # Check if date is today or tomorrow (for demo purposes, we return data for these dates)
    today = date.today()
    tomorrow = today + timedelta(days=1)
    
    if date_str in [today.isoformat(), tomorrow.isoformat()]:
        if court_id in SAMPLE_CAUSE_LISTS:
            response = SAMPLE_CAUSE_LISTS[court_id].copy()
            response["date"] = date_str
            response["state"] = state or "Andhra Pradesh"
            response["district"] = district or "Kadapa"
            return jsonify(response)
    
    # Return empty cause list for other dates
    return jsonify({
        "court_name": f"Court {court_id}",
        "court_id": court_id,
        "date": date_str,
        "cases": []
    })


@app.route('/pdf/<filename>', methods=['GET'])
def get_pdf(filename):
    """Mock PDF endpoint - returns a message instead of actual PDF"""
    return jsonify({
        "message": f"This is a mock PDF endpoint for {filename}",
        "note": "In production, this would return actual PDF bytes"
    })


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "message": "Mock eCourts API Server is running",
        "available_courts": list(SAMPLE_CAUSE_LISTS.keys())
    })


if __name__ == '__main__':
    print("=" * 60)
    print("Mock eCourts API Server Starting...")
    print("=" * 60)
    print("Server URL: http://localhost:5001")
    print("\nAvailable endpoints:")
    print("  - GET  /health")
    print("  - GET  /cnr/<cnr>")
    print("  - GET  /cause-list?court_id=101&date=2025-10-19")
    print("\nSample CNRs for testing:")
    for court_id, court_data in SAMPLE_CAUSE_LISTS.items():
        print(f"\n  Court {court_id} ({court_data['court_name']}):")
        for case in court_data['cases']:
            print(f"    - {case['cnr']} ({case['case_no']})")
    print("\n" + "=" * 60)
    print("Set your CLI to use: set ECOURTS_API_BASE=http://localhost:5001")
    print("=" * 60 + "\n")
    
    app.run(host='localhost', port=5001, debug=True)
