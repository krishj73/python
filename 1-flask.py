from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello():
    return "Hello World" #can also insert html code

if (__name__=='__main__'):
    app.run(debug=True)