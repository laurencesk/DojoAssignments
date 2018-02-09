from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def index():
    session['counter']  +=1
    return render_template('index.html')

@app.route('/refresh',methods=['GET'])
def refresh():
    session['counter']  +=1
    return redirect('/')

@app.route('/reset',methods=['GET'])
def reset():
    session['counter'] = 1
    return render_template('index.html')

app.run(debug = True)
