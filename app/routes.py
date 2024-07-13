from flask import Flask, render_template
from flask import render_template, flash, redirect, url_for
from app import app
from app.models import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return (render_template('index.html'))

@app.route('/data_view')
def data_view():
    return(render_template('data_view.html'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title = "Sign in", form = form)