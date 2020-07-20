from flask import Flask, redirect, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

responses = []

@app.route('/')
def home():
    return render_template('index.html', title=satisfaction_survey.title)

@app.route('/questions/<int:question_id>')
def question(question_id):
    question = satisfaction_survey.questions[question_id]
    return render_template('question.html', question=question)