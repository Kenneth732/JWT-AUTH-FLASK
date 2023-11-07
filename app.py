from flask import Flask, render_template

app = Flask(__name__)

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
