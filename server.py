from flask import Flask, render_template, request, redirect, session
from flask import Markup
import random
app = Flask(__name__)
app.secret_key = 'ThisIsASecretKey'

@app.route('/') #This is the root
def index():
    if not ('style' in session):
        session['style'] = 'white'
    if not ('serverGenNum' in session):
         session['serverGenNum'] = random.randrange(1,101)
    messages = ""
    colorbox = ""
    return render_template('index.html')

@app.route('/guessNum', methods =['POST'])
def guessNum():
    guess = int(request.form['guess'])
    button = str(request.form['button'])
    if int(guess) == int(session['serverGenNum']):
        message = str(session['serverGenNum']) + " was the number!"
        colorbox = 'green'
        button = Markup('<a href="/restart">Play again!</a>')
    if int(guess) < session['serverGenNum']:
        message = "Too Low"
        colorbox = 'red'
    if int(guess) > session['serverGenNum']:
        message = "Too High"
        colorbox = 'red'
    return render_template('index.html', message = message, colorbox = colorbox, button = button)

@app.route('/restart')
def restart():
	session.pop('serverGenNum')
	return redirect('/')

app.run(debug=True)