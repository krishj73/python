from flask import Flask

app = Flask(__name__)       #creates flask app object, name tells where the flask app is stored

@app.route('/')             #maps url to function
def func():
    return "Hello World"

@app.route('/about')
def about():
    return "About page"

@app.route('/<name>')
def hello(name):
    return f"Hello {name}"

if __name__ == '__main__':
    app.run(debug=True)     #starts flask dev server, shows error in browser if any