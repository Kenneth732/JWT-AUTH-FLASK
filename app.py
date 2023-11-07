from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

app.config['SECRET_KEY'] = 'a018ddb39a56d24e179255f0fa7f509ff9b215a905cbf1a15e56a32b465e319a542227eb50d3428de14d51c27c17d775852cf14ab0'

@app.route('/')
def home():
    return render_template('index.html')  # Replace 'index.html' with the name of your HTML template

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/regester')
def regester():
    return render_template('regester.html')


if __name__ == '__main__':
    app.run(debug=True)
