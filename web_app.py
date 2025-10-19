"""
eCourts Listing Checker - Web Interface
A modern web application for checking court case listings
"""
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for, send_file
from datetime import date, timedelta
import os

from src.ecourts_api import EcourtsAPI, EcourtsAPIError
from src.utils import dates_for_when, save_json
from src.cli import build_case_no, find_case_in_causelist
from src.downloader import download_file

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Initialize API (check for offline mode from environment)
# Default to offline mode (using sample data) unless explicitly set to online
offline_mode = os.getenv("OFFLINE_MODE", "true").lower() == "true"
# Get API base URL from environment (for mock server support)
api_base = os.getenv("ECOURTS_API_BASE")
api = EcourtsAPI(base=api_base, offline_mode=offline_mode)


@app.route('/')
def index():
    """Home page with search form"""
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    """Handle search form submission"""
    try:
        # Get form data
        cnr = request.form.get('cnr', '').strip()
        case_type = request.form.get('case_type', '').strip()
        case_number = request.form.get('case_number', '').strip()
        case_year = request.form.get('case_year', '').strip()
        when = request.form.get('when', 'today')
        court_id = request.form.get('court_id', '').strip()
        state = request.form.get('state', '').strip()
        district = request.form.get('district', '').strip()
        
        # Validation
        if not cnr and not (case_type and case_number and case_year):
            flash('Please provide either CNR or Case Type/Number/Year', 'error')
            return redirect(url_for('index'))
        
        if not court_id:
            flash('Court ID is required', 'error')
            return redirect(url_for('index'))
        
        # Build case number if not using CNR
        case_no = build_case_no(case_type, case_number, case_year) if not cnr else None
        
        # Get dates to check
        dates = dates_for_when(when)
        
        # Search results
        results = {
            'query': {
                'cnr': cnr,
                'case_no': case_no,
                'when': when,
                'court_id': court_id,
                'state': state,
                'district': district
            },
            'found': False,
            'listings': []
        }
        
        for d in dates:
            date_str = d.isoformat()
            try:
                causelist = api.get_cause_list(
                    court_id=court_id,
                    date_str=date_str,
                    state=state,
                    district=district
                )
                
                if causelist:
                    hits = find_case_in_causelist(causelist, cnr=cnr, case_no=case_no)
                    
                    for h in hits:
                        entry = {
                            'date': date_str,
                            'court_name': (causelist.get('court_name') if isinstance(causelist, dict) else None) or court_id,
                            'serial_no': h.get('serial_no') or h.get('sl_no') or h.get('sr_no'),
                            'case': h
                        }
                        results['listings'].append(entry)
                        results['found'] = True
            
            except EcourtsAPIError as e:
                flash(f'Error fetching data for {date_str}: {str(e)}', 'warning')
        
        return render_template('results.html', results=results)
    
    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'error')
        return redirect(url_for('index'))


@app.route('/api/search', methods=['POST', 'GET'])
def api_search():
    """JSON API endpoint for programmatic access"""
    try:
        # Get parameters from JSON or query string
        payload = request.json or request.values
        
        cnr = payload.get('cnr', '').strip()
        case_type = payload.get('case_type', '').strip()
        case_number = payload.get('number', '').strip()
        case_year = payload.get('year', '').strip()
        when = payload.get('when', 'today')
        court_id = payload.get('court_id', '').strip()
        state = payload.get('state', '').strip()
        district = payload.get('district', '').strip()
        
        # Validation
        if not cnr and not (case_type and case_number and case_year):
            return jsonify({'error': 'Please provide either CNR or Case Type/Number/Year'}), 400
        
        if not court_id:
            return jsonify({'error': 'Court ID is required'}), 400
        
        # Build case number
        case_no = build_case_no(case_type, case_number, case_year) if not cnr else None
        
        # Get dates
        dates = dates_for_when(when)
        
        # Search
        results = {'found': False, 'listings': []}
        
        for d in dates:
            date_str = d.isoformat()
            try:
                causelist = api.get_cause_list(
                    court_id=court_id,
                    date_str=date_str,
                    state=state,
                    district=district
                )
                
                if causelist:
                    hits = find_case_in_causelist(causelist, cnr=cnr, case_no=case_no)
                    
                    for h in hits:
                        entry = {
                            'date': date_str,
                            'court': causelist.get('court_name') if isinstance(causelist, dict) else court_id,
                            'serial_no': h.get('serial_no') or h.get('sl_no') or h.get('sr_no'),
                            'case': h
                        }
                        results['listings'].append(entry)
                        results['found'] = True
            
            except EcourtsAPIError as e:
                return jsonify({'error': str(e)}), 500
        
        return jsonify(results)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/causelist', methods=['GET', 'POST'])
def causelist():
    """View full cause list for a court/date"""
    if request.method == 'GET':
        return render_template('causelist.html')
    
    try:
        court_id = request.form.get('court_id', '').strip()
        when = request.form.get('when', 'today')
        state = request.form.get('state', '').strip()
        district = request.form.get('district', '').strip()
        
        if not court_id:
            flash('Court ID is required', 'error')
            return redirect(url_for('causelist'))
        
        dates = dates_for_when(when)
        all_lists = []
        
        for d in dates:
            date_str = d.isoformat()
            try:
                causelist_data = api.get_cause_list(
                    court_id=court_id,
                    date_str=date_str,
                    state=state,
                    district=district
                )
                
                if causelist_data:
                    all_lists.append({
                        'date': date_str,
                        'court_name': causelist_data.get('court_name', f'Court {court_id}'),
                        'cases': causelist_data.get('cases', [])
                    })
            
            except EcourtsAPIError as e:
                flash(f'Error fetching cause list for {date_str}: {str(e)}', 'warning')
        
        return render_template('causelist_results.html', causelists=all_lists, court_id=court_id)
    
    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'error')
        return redirect(url_for('causelist'))


@app.route('/about')
def about():
    """About page"""
    return render_template('about.html', offline_mode=offline_mode)


@app.route('/api/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'offline_mode': offline_mode,
        'message': 'eCourts Listing Checker Web App is running'
    })


@app.route('/download/pdf/<case_id>')
def download_pdf(case_id):
    """Download PDF for a case"""
    try:
        # In offline mode, generate a sample PDF
        if offline_mode:
            from reportlab.lib.pagesizes import letter
            from reportlab.pdfgen import canvas
            from reportlab.lib.units import inch
            import io
            
            # Create PDF in memory
            buffer = io.BytesIO()
            c = canvas.Canvas(buffer, pagesize=letter)
            width, height = letter
            
            # Add content
            c.setFont("Helvetica-Bold", 16)
            c.drawString(1*inch, height - 1*inch, "eCourts - Case Details")
            
            c.setFont("Helvetica", 12)
            y = height - 1.5*inch
            
            # Sample case details based on case_id
            case_details = {
                '123': {
                    'cnr': 'ABCD1234567890123',
                    'case_no': 'CIV 123/2024',
                    'case_type': 'Civil',
                    'parties': 'Ram Kumar vs Shyam Singh',
                    'advocate': 'Adv. Rajesh Sharma',
                    'purpose': 'Final Arguments'
                },
                '456': {
                    'cnr': 'WXYZ9876543210987',
                    'case_no': 'CRLP 456/2023',
                    'case_type': 'Criminal',
                    'parties': 'State vs Mohan Lal',
                    'advocate': 'Adv. Priya Verma',
                    'purpose': 'Hearing'
                },
                '789': {
                    'cnr': 'PQRS5555666677778',
                    'case_no': 'CIV 789/2024',
                    'case_type': 'Civil',
                    'parties': 'Lakshmi Devi vs Municipal Corporation',
                    'advocate': 'Adv. Suresh Kumar',
                    'purpose': 'Evidence'
                }
            }
            
            details = case_details.get(case_id, case_details['123'])
            
            c.drawString(1*inch, y, f"CNR: {details['cnr']}")
            y -= 0.3*inch
            c.drawString(1*inch, y, f"Case Number: {details['case_no']}")
            y -= 0.3*inch
            c.drawString(1*inch, y, f"Case Type: {details['case_type']}")
            y -= 0.3*inch
            c.drawString(1*inch, y, f"Parties: {details['parties']}")
            y -= 0.3*inch
            c.drawString(1*inch, y, f"Advocate: {details['advocate']}")
            y -= 0.3*inch
            c.drawString(1*inch, y, f"Purpose: {details['purpose']}")
            y -= 0.5*inch
            
            c.setFont("Helvetica-Italic", 10)
            c.drawString(1*inch, y, "Court: District Court - Kadapa")
            y -= 0.3*inch
            c.drawString(1*inch, y, "Date: 2025-10-19")
            
            c.save()
            buffer.seek(0)
            
            return send_file(
                buffer,
                mimetype='application/pdf',
                as_attachment=True,
                download_name=f'case_{case_id}.pdf'
            )
        else:
            flash('PDF download not available in online mode', 'warning')
            return redirect(url_for('index'))
    
    except Exception as e:
        flash(f'Error generating PDF: {str(e)}', 'error')
        return redirect(url_for('index'))


if __name__ == '__main__':
    print("=" * 60)
    print("eCourts Listing Checker - Web Interface")
    print("=" * 60)
    print(f"Mode: {'OFFLINE (using sample data)' if offline_mode else 'ONLINE (using API)'}")
    if api_base:
        print(f"API Base URL: {api_base}")
    print("URL: http://localhost:5000")
    print("=" * 60)
    app.run(host='0.0.0.0', port=5000, debug=True)
