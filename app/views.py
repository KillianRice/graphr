from app import app
from flask import render_template, flash, redirect, request, json, jsonify
from graphr import graphr
from numpy import random
from datetime import datetime
import verdi_config

c = sorted(verdi_config.COMMANDS.keys())[:6]

#c = ['a', 'b', 'c', 'd', 'e', 'f'];

def getplot():
    f = 'data/data.txt'
    img_path = 'static/graph.svg'
    img_data = graphr.graph_data(f,img_path)
    return img_data


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
    datefmt = '%Y-%m-%d %H:%M:%S.%f'
    n = request.args.get('n', 0, type=int)
    names = request.args.getlist('i[]')
    data = {}
    data['x'] = datetime.now().strftime(datefmt)
    for name in names:
        data[name] = random.randn()

    return jsonify(**data)

@app.route('/js')
def js():
    return render_template('js.html', commands = c)









