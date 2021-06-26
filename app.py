from flask import Flask, render_template, redirect, flash
from flask_wtf import form
from forms import LoginForm, TextForm, NumForm
from config import Config
from dbsubmission import BasicSubmission
app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TextForm()
    if form.validate_on_submit():
        basicSubmission = BasicSubmission(form.answer1.data)
        print(form.answer1.data)
        return redirect('/home')
    return render_template('index.html', title='Form', form=form)

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
