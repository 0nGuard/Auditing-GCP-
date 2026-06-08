{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, jsonify\
\
app = Flask(__name__)\
\
@app.route("/")\
def home():\
    return "GridWatch Lite - Energy Monitoring Dashboard"\
\
@app.route("/status")\
def status():\
    return jsonify(\{\
        "region": "EU-West",\
        "grid_load": "72%",\
        "stability": "Stable",\
        "last_updated": "2026-07-01T10:00:00Z"\
    \})\
\
@app.route("/metrics")\
def metrics():\
    return jsonify(\{\
        "voltage": "230V",\
        "frequency": "50Hz",\
        "uptime": "99.98%"\
    \})\
\
@app.route("/admin")\
def admin():\
    return jsonify(\{\
        "note": "Finance reports stored in GCS bucket",\
        "bucket": "gs://fin-reports-internal/",\
        "access": "via shared service account"\
    \})\
\
if __name__ == "__main__":\
    app.run(host="0.0.0.0", port=8080)}
