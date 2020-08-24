from flask import Flask, flash, redirect, render_template, \
     request, url_for
from utils import get_countries
from client import Corona
import numpy as np
import pandas as pd
import wbdata as wb
import datetime
import os

graph_folder = os.path.join('static', 'graphs')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = graph_folder
data_path = './static/'
countries = get_countries()

@app.route('/')
def index():
    return render_template(
        'index.html',
        dropdown_list=countries)

@app.route('/plot', methods=['GET', 'POST'])
def show_index():
    select = request.form.get('comp_select')
    cor = Corona()
    cor.plot(select)
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'graph*.png')
    return render_template("plot.html", user_image=full_filename)

if __name__ == '__main__':
    app.run()