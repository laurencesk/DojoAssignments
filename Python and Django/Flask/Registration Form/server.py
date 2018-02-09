from flask import Flask, request, redirect, render_template, session,flash
import re
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    return render_template('index.html')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/response',  methods=['POST'])
def response():
    error = 0

    session['email'] = request.form['email']
    if EMAIL_REGEX.match(session['email']):
        pass
    else:
        flash('Format of the email addres you entered is not valid')
        error+=1

    session['firstName'] = request.form['firstName']
    if session['firstName'].isalpha():
        pass
    else:
        flash('First name cannot be empty')
        error+=1

    session['lastName'] = request.form['lastName']
    if session['lastName'].isalpha():
        pass
    else:
        flash('Last name cannot be empty')
        error+=1

    session['password'] = request.form['password']
    if len(session['password'])>=7:
        pass
    else:
        flash('Password needs to be at least 8 characters long')
        error+=1

    session['confirmPassword'] = request.form['confirmPassword']
    if (session['confirmPassword'])==session['password']:
        pass
    else:
        flash('Your two entries do not match')     
        error+=1

    if error == 0:
        return render_template('response.html')
    else:
        return render_template('index.html')

app.run(debug=True)
