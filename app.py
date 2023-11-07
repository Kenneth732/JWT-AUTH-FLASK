import os
from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)

# Set the database URI and configurations before initializing db
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'a018ddb39a56d24e179255f0fa7f509ff9b215a905cbf1a15e56a32b465e319a542227eb50d3428de14d51c27c17d775852cf14ab0'

db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False unique=True)
    password = db.Column(db.String(80), nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')  # Corrected the route
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
