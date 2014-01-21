import os
from flask import Flask
import pymongo

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', name=name)