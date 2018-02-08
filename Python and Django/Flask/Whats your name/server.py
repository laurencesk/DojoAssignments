from flask import Flask, request, redirect, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    username = request.form['name']
    print username
    return redirect('/')

app.run(debug=True)
