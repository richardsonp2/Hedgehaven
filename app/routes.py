from flask import Flask, render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return (render_template('index.html'))

@app.route('/data_view')
def data_view():
    return(render_template('data_view.html'))