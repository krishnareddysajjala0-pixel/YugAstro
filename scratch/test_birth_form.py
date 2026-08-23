# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro")

from app import app

client = app.test_client()

print("=== TESTING BIRTH FORM POST TO /chart ===")
post_data = {
    "name": "Krishna",
    "dob": "1995-05-15",
    "tob": "10:30",
    "place": "Hyderabad, Telangana, India",
    "lat": "17.3850",
    "lon": "78.4867"
}

resp = client.post('/chart', data=post_data, follow_redirects=True)
print("POST /chart Status Code:", resp.status_code)
if resp.status_code == 200:
    print("Found 'కుండలి' or 'లగ్నం' in output:", ("లగ్నం" in resp.data.decode('utf-8') or "Lagnam" in resp.data.decode('utf-8')))

print("=== TESTING BIRTH FORM DEFAULT ACTION /go-to-birth-chart ===")
resp_default = client.get('/go-to-birth-chart', follow_redirects=True)
print("GET /go-to-birth-chart Status Code:", resp_default.status_code)
