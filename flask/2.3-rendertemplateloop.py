from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def subjects():
    subjects = ["C", "C++", "Java", "Python"]
    return render_template("subjects.html", subjects = subjects)    #subjects = ["C", "C++", "Java", "Python"]

if __name__ == '__main__':
    app.run(debug=True)