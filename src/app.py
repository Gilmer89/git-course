from flask import Flask

app = Flask( __name__)

@app.route('/')
def index():
    return "Bye Alfonso!"

@app.route('/sum/<int:num1>/<int:num2>')
def sum(a: int, b: int):
    return a +b