from flask import Flask, request, redirect, render_template, session,flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/response', methods=['POST'] )
def response():
    error = 0
    session['name'] = request.form['name']
    if len(session['name']) <1:
        flash('Your name cannot be empty')
        error +=1
    else:
        pass
    session['language'] = request.form['language']
    if len(session['language']) <1:
        flash('Your language cannot be empty')
        error +=1
    else:
        pass
    session['location'] = request.form['location']
    if len(session['location']) <1:
        flash('Your location cannot be empty')
        error +=1
    else:
        pass
    session['comment'] = request.form['comment']
    if len(session['comment']) >120:
        flash('The maximun charactor cannot exceed 120')
        error +=1
    else:
        pass

    if error==0:    
        return render_template('response.html')
    else:
        return render_template('index.html')

app.run(debug = True)

