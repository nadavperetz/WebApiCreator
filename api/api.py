import os

from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy


tmpl_dir = os.path.abspath(__file__ + "/../../templates")
app = Flask(__name__, template_folder=tmpl_dir)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models.results import Result


@app.route('/', methods=['GET'])
def hello_world():
    errors = []
    results = {}
    return render_template('index.html', errors=errors, results=results)


@app.route('/<name>', methods=['GET', 'POST'])
def hello_name(name):
    if request.method == "POST":
        return str(request.data)
    else:
        return 'Hello {0}'.format(name)


if __name__ == '__main__':
    app.run()



