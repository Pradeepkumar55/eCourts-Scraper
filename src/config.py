"""
Config file. Set API_BASE to the public eCourts JSON API base URL you choose.
If you have an environment variable `ECOURTS_API_BASE` it overrides this value.

The sample default is a placeholder; you should set this to a working public API URL.
"""
import os

API_BASE = os.getenv("ECOURTS_API_BASE") or "https://example-ecourts-api.example.com"
# Timeout settings
REQUEST_TIMEOUT = 20

# If your API needs an API key, put it here or via env var
API_KEY = os.getenv("ECOURTS_API_KEY") or None

# Default output folders
OUTPUT_DIR = os.path.join(os.getcwd(), "outputs")
DOWNLOAD_DIR = os.path.join(os.getcwd(), "downloads")


# Example endpoint templates (update these to match your API provider)
# These are used by src/ecourts_api.py -- adapt if your API uses different paths.
ENDPOINTS = {
    "cnr_search": "/cnr/{cnr}",
    "cause_list": "/cause-list",  # expects params: court_id, date
}
