#!/usr/bin/env python
# coding=utf-8

from flask import Flask, Response, render_template
import json
from database import DataManager

app = Flask("SuperTaxiReturns")
db  = DataManager()

@app.route("/v1/api")
def api_home():
    return render_template("api.html")

app.run(host="0.0.0.0",port=5000)
