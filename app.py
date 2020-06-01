from flask import Flask,render_template,request
import os

from readxls import read

app = Flask(__name__)

@app.route('/')
def homepage():
    content = 'content'
    rd = read()
    return render_template("index.html",content = rd)


if __name__ == "__main__":
    app.run(host='localhost',port=80,debug=True)
