from app import app
from flask import render_template, flash, redirect, request
import graphr

def getplot():
    f = 'data.txt'
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
