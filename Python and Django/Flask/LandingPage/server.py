from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/dojos/new')
def form():
    # name = request.form['name']
    # email = request.form['email']
    # # print neme, email
    # return redirect('/dojos/new.html')
    return render_template('/dojos/new.html')

@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   # name = request.form['name']
   # email = request.form['email']
   # redirects back to the '/' route
   return redirect('/')


app.run(debug = True)
