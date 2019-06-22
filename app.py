from flask import Flask
from flask import request
from flask import make_response
app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Hello World!</h1><p>Your browser is {}</p>'.format(user_agent)

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/cookie')
def cookie():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', 42)
    return response

@app.route('/req')
def req():
    return '<h1>Bad Request</h1>', 400


# if __name__ == '__main__':
#     app.run(debug=True)
