#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
if __name__ == '__main__':
    app.run(port=5555, debug=True)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:string>')
def print_string(string):
    print(string)
    return f'{string}'

@app.route('/count/<int:num>')
def count(num):
    numbers = (((str(i) + '\n') for i in range(0, num)))
    return numbers
        

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, num2, operation):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2

    else:
        result = num1 % num2
    
    return f'{result}'
