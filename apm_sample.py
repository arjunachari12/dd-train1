from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/error')
def trigger_error():
    # Introducing a division by zero error
    result = 1 / 0
    return jsonify({"result": result})

@app.route('/random_error')
def random_error():
    # Randomly raising an exception
    if random.choice([True, False]):
        raise ValueError("This is a random ValueError!")
    return 'No error this time!'

if __name__ == '__main__':
    app.run(debug=True)
