from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def result():
    marks = 70
    return render_template("result.html", marks = marks)    #marks = 70

if __name__ == '__main__':
    app.run(debug=True)