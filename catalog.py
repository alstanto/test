import os
from flask import Flask
import pymongo

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the data catalog again'