from app import app
from flask import render_template, flash, redirect, request, json, jsonify
from graphr import graphr
from numpy import random
from datetime import datetime
import verdi_config
import pandas as pd

#c = sorted(verdi_config.COMMANDS.keys())[:6]

c = ['a', 'b', 'c', 'd'];

def getplot():
    f = 'data/data.txt'
    img_path = 'static/graph.svg'
    img_data = graphr.graph_data(f,img_path)
    return img_data


@app.route('/')
@app.route('/index', methods = ['GET','POST'])
def index():
    return render_template('hello world')

@app.route('/update')
def update():
    img_data = getplot()
    return img_data

@app.route('/get_json')
def get_json():
    df = pd.read_csv('most_recent.txt', sep='\t', index_col=0, parse_dates=True)
    datefmt = '%Y-%m-%d %H:%M:%S.%f'
    n = request.args.get('n', 0, type=int)
    names = request.args.getlist('i[]')
    data = {}
    data['x'] = str(df.index[0])
    print(data['x'])
    print(type(data['x']))
    for name in names:
        data[name] = float(df[name])

    return jsonify(**data)

@app.route('/js')
def js():
    return render_template('js.html', commands = c)

@app.route('/verdi')
def verdi():
    return render_template('verdi_monitor.html')







