"""
Thin wrapper around the configured public eCourts JSON API.
Adapt the endpoint templates in src/config.py to match the API you use.
"""
import os
import json
import requests
from urllib.parse import urljoin
from .config import API_BASE, REQUEST_TIMEOUT, ENDPOINTS, API_KEY


class EcourtsAPIError(Exception):
    pass


class EcourtsAPI:
    def __init__(self, base=None, api_key=None, offline_mode=False):
        self.base = base or API_BASE
        self.api_key = api_key or API_KEY
        self.offline_mode = offline_mode or os.getenv("OFFLINE_MODE") == "true"
        self.sample_data_dir = os.path.join(os.getcwd(), "sample_data")

    def _get(self, path, params=None):
        url = urljoin(self.base, path)
        headers = {}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        try:
            r = requests.get(url, params=params, headers=headers, timeout=REQUEST_TIMEOUT)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            raise EcourtsAPIError(f"HTTP error: {e} - {getattr(e, 'response', None)}")
        except ValueError:
            # JSON decode error
            raise EcourtsAPIError("Invalid JSON response from API")
        except Exception as e:
            raise EcourtsAPIError(f"Request failed: {e}")

    def search_by_cnr(self, cnr):
        path = ENDPOINTS.get("cnr_search").format(cnr=cnr)
        return self._get(path)

    def get_cause_list(self, court_id: str, date_str: str, state=None, district=None):
        # If offline mode, load from sample data files
        if self.offline_mode:
            return self._load_sample_causelist(court_id, date_str)
        
        # Many APIs accept court_id & date params; adapt param names as needed.
        path = ENDPOINTS.get("cause_list")
        params = {"court_id": court_id, "date": date_str}
        if state:
            params["state"] = state
        if district:
            params["district"] = district
        return self._get(path, params=params)
    
    def _load_sample_causelist(self, court_id: str, date_str: str):
        """Load cause list from local sample data files"""
        # Try to find a matching sample file
        filename = f"causelist_{court_id}_today.json"
        filepath = os.path.join(self.sample_data_dir, filename)
        
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Update the date to match requested date
                data['date'] = date_str
                return data
        else:
            # Return empty cause list if no sample file found
            return {
                "court_name": f"Court {court_id}",
                "court_id": court_id,
                "date": date_str,
                "cases": []
            }
