from flask import Flask, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
     # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function.
def hello_world():
  return 'Hello World! My name is Laurence'  # Return the string 'Hello World!' as a response.
# app.run(debug=True)      # Run the app in debug mode.

@app.route('/projects')          # The "@" symbol designates a "decorator" which attaches the following

def projects():
  return render_template('projects.html')  # Return the string 'Hello World!' as a response.

@app.route('/about')          # The "@" symbol designates a "decorator" which attaches the following

def about():
  return render_template('about.html')  # Return the string 'Hello World!' as a response.

app.run(debug=True)
