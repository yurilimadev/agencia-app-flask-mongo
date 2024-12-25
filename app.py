from dotenv import dotenv_values
from flask import Flask, render_template, url_for
from flask_pymongo import PyMongo
app = Flask(__name__)

config = dotenv_values(".env")
print(config)
app.config['MONGO_URI'] = config['MONGO_URI']
mongo = PyMongo(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/area-admin')
def login():
    return render_template('area-admin.html')
