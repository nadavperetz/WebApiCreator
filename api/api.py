import os

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy


tmpl_dir = os.path.abspath(__file__ + "/../../templates")
app = Flask(__name__, template_folder=tmpl_dir)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models.results import Result


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()



