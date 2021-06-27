from flask import Flask, render_template, redirect, flash, request
from flask_wtf import form
from forms import LoginForm, TextForm, NumForm
from config import Config
from dbsubmission import BasicSubmission

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title='Form')

@app.route('/home', methods= ['POST'])
def home():
    q1 = request.form.get("question1")
    ch1 = request.form.get("check1")
    ch2 = request.form.get("check2")
    print(q1)
    print(ch1)
    print(ch2)
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
