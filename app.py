from flask import Flask, render_template, redirect, flash, request
from flask_wtf import form
from forms import LoginForm, TextForm, NumForm
from config import Config
from dbsubmission import BasicSubmission

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET'])
def index():
    return render_template('form.html', title='Form')

@app.route('/home', methods= ['POST'])
def home():
    submission = BasicSubmission(request.form)
    submission.PrintAll()
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
