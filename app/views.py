from app import app
from flask import render_template, flash, redirect, request, json, jsonify
from graphr import graphr
from numpy import random

def getplot():
    f = 'data/data.txt'
    img_path = 'static/graph.svg'
    img_data = graphr.graph_data(f,img_path)
    return img_data
def makejson(data):
    return jsonify(data)


@app.route('/')
@app.route('/index', methods = ['GET','POST'])
def index():
    img_data = getplot()
    return render_template('index.html',img_data=img_data)

@app.route('/update')
def update():
    img_data = getplot()
    return img_data

@app.route('/get_json')
def get_json():
    data = {
            'x': random.randn(),
            'y': random.randn()
        }

    return jsonify(**data)

@app.route('/js')
def js():
    return render_template('js.html')









