from flask import Flask, render_template
from models import db
from api import api_bp
import argparse

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)
app.register_blueprint(api_bp)


@app.route('/')
def index():
    return render_template('index.html')


def init():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--init', dest='init', action='store_true')
    args = parser.parse_args()
    if args.init:
        init()
    else:
        app.run(host='0.0.0.0', port=3000)  # I like port 3000 :)