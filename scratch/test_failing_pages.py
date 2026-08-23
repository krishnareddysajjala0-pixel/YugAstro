# -*- coding: utf-8 -*-
import sys, os, traceback
sys.path.insert(0, r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro")

from app import app

client = app.test_client()

routes_to_test = [
    '/daily_panchangam',
    '/calendar_view',
    '/dwadasa_graha_visheshalu',
    '/go-to-birth-chart',
    '/'
]

for r in routes_to_test:
    print(f"=== TESTING ROUTE: {r} ===")
    try:
        resp = client.get(r, follow_redirects=True)
        print(f"Status Code for {r}: {resp.status_code}")
        if resp.status_code != 200:
            print("Response text sample:", resp.data.decode('utf-8')[:500])
    except Exception as e:
        print(f"EXCEPTION for {r}: {e}")
        traceback.print_exc()
