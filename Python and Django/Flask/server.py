from flask import Flask, render_template, request, redirect,session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

def setNum():
    session['num'] = random.randrange(0, 101)


@app.route('/')
def index():
    if "num" not in session:
        setNum()
    else:
        pass
    return render_template('index.html')

@app.route('/guess', methods = ['POST'])
def guess():
    display = ""
    if request.form['guess'].isdigit():
        if int(request.form['guess']) == session['num']:
            session['display'] = "Correct"
            return render_template('index.html')

        elif int(request.form['guess']) > session['num']:
             session['display'] = "Too High"
        elif int(request.form['guess']) < session['num']:
             session['display'] = "Too Low"      
    else:
         session['display'] = "It's not a valid number"
    return render_template('index.html')



app.run(debug = True)