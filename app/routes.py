from flask import render_template
from . import app

@app.route('/')
def index():
    return render_template('index.html', active_page='home')

@app.route('/academics')
def academics():
    return render_template('academics.html',  active_page='academics')

@app.route('/robotics')
def robotics():
    return render_template('robotics.html',  active_page='robotics')

@app.route('/contact')
def contact():
    return render_template('contact.html', )

@app.route('/entrepreneurship')
def entre():
    return render_template('entrepreneurship.html',  active_page='entrepreneurship')

@app.route('/teaching')
def teaching():
    return render_template('teaching.html',  active_page='teaching')

