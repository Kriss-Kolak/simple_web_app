from flask import Flask, render_template, redirect
from scraper import scrap

app = Flask(__name__)




@app.route('/')
def home():
    data = scrap()
    return render_template('home.html', data = data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)