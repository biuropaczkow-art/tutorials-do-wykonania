#!/usr/bin/env python3
"""Serwis Flask dla przeglądania tutoriali z playlisty 'Do wykonania'"""

from flask import Flask, render_template, jsonify
import markdown
from pathlib import Path

app = Flask(__name__)

TUTORIALS_DIR = Path(__file__).parent / "tutorials"

@app.route("/")
def index():
    """Strona główna z listą tutoriali"""
    tutorials = []
    for f in sorted(TUTORIALS_DIR.glob("tutorial_*.md")):
        num = f.stem.split("_")[1]
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            title = content.split('## ')[1].split('\n')[0] if '## ' in content else f.stem
        tutorials.append({'number': num, 'title': title, 'file': f.name})
    return render_template('index.html', tutorials=tutorials)

@app.route("/tutorial/<int:number>.md")
def view_tutorial(number):
    """Podgląd konkretnego tutoriala"""
    file_path = TUTORIALS_DIR / f"tutorial_{number}.md"
    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        html = markdown.markdown(content, extensions=['fenced_code', 'toc'])
        return f"<html><body>{html}</body></html>"
    return "Tutorial not found", 404

@app.route("/api/tutorials")
def api_tutorials():
    """API z listą tutoriali"""
    tutorials = []
    for i, f in enumerate(sorted(TUTORIALS_DIR.glob("tutorial_*.md")), 1):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            title = content.split('## ')[1].split('\n')[0] if '## ' in content else f.stem
        tutorials.append({'number': i, 'title': title, 'progress': 100})
    return jsonify(tutorials)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)