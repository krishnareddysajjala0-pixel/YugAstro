# -*- coding: utf-8 -*-
import glob, os
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader(r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro\templates"))

templates = glob.glob(r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro\templates\*.html")

for t in templates:
    name = os.path.basename(t)
    try:
        env.get_template(name)
        print(f"[OK] {name}")
    except Exception as e:
        print(f"[ERROR] {name}: {e}")
