from flask import Flask, redirect, request, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST': 
        session['responses'] = []
        return redirect('/questions/0')
    else:
        return render_template('index.html', title=satisfaction_survey.title)

@app.route('/questions/<int:question_id>')
def question(question_id):
    responses = session.get('responses')
    if (question_id != len(responses)):
        flash('Oops! Invalid question. Please continue here.')
        return redirect(f'/questions/{len(responses)}')
    
    if question_id == len(satisfaction_survey.questions):
        return redirect('/thanks')

    question = satisfaction_survey.questions[question_id]
    return render_template('question.html', question=question)
        

@app.route('/answer', methods=['POST'])
def save_answer():
    responses = session.get('responses')
    answer = request.form['answer']
    responses.append(answer)
    session['responses'] = responses
    id = len(responses)
    return redirect(f'/questions/{id}')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')