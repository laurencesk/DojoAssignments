from flask import Flask, request, redirect, session, render_template
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity' not in session:
        session['activity'] = []
    return render_template('index.html')

@app.route('/process_money', methods = ['POST'])
def process():
    if request.form['action'] == 'farm':
        gold = random.randrange(10, 21)
        session['gold'] += gold
        session['activity'] .append(['Earned '+str(gold)+' golds from the farm!'])
        print gold, session['gold']
    elif request.form['action'] == 'Cave':
        gold = random.randrange(5, 11)
        session['gold'] += gold
        session['activity']. append(['Earned '+str(gold)+' golds from the cave!'])
        print gold, session['gold']

    elif request.form['action'] == 'House':
        gold = random.randrange(2, 6)
        session['gold'] += gold
        session['activity'] .append(['Earned '+str(gold)+' golds from the house!'])
        print gold, session['gold']

    elif request.form['action'] == 'Casino':
        gold = random.randrange(-50, 51)
        session['gold'] += gold
        if gold >0:    
            session['activity'].append(['Entered a casino and earned '+str(gold)+' golds!'])
        else:
            session['activity'].append(['Entered a casino and lost '+str(-gold)+' golds...Ouch..'])


    return redirect('/')




app.run(debug = True)
