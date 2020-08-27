from flask import Flask, render_template, request
from utils import get_countries
from client import Corona
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
    corona = Corona()
    corona.generate_plot(select)
    filename = f'static/graphs/graph{datetime.datetime.now().timestamp()}.png'
    corona.plt.savefig(filename, dpi=300)
    return render_template("plot.html", user_image=filename)

if __name__ == '__main__':
    app.run()