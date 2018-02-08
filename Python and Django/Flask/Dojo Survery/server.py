from flask import Flask, request, redirect, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/response', methods=['POST'] )
def response():
    name = request.form['name']
    language = request.form['language']
    location = request.form['location']
    comment = request.form['comment']
    return render_template('response.html', name=name,language=language,location=location,comment=comment)

app.run(debug = True)

