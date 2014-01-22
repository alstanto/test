import os
from flask import Flask, render_template, request
from flask.ext import restful

import pymongo

app = Flask(__name__)
api = restful.Api(app)


class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/hello_world')


@app.route('/')
def home():
    users = 'Ash'
    return render_template('home.html', users=users)


@app.route('/create_template')
def template_elements():

    return 'template elements json'


@app.route('/test')
def test():
    a = request.args
    s=''
    for key in a:
       elem =  key + '=' + a[key] +', '
       s += elem
    return 'this is the request...' + s


@app.route('/get_template')
def get_template():
    return 'here is the object you requested... [json goes here]'


if __name__ == '__main__':

    app.run(debug=True)