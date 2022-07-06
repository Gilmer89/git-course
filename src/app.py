from flask import Flask

app = Flask( __name__)

@app.route('/')
def index():
    return "Bye code!"

@app.route('/hello')
def greating():
    return "Hello World!"

@app.route('/sum/<int:a>/<int:b>')
def sum(a: int, b: int):
    nums_sum = a +b
    return f"la suma es: {str(nums_sum)}"

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a: int, b: int):
    result = float(a*b)
    return f"el resultado de la multiplicacion es:{str(result)}"
