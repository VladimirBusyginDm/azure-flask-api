from flask import Flask, jsonify
import random

application = Flask(__name__)

answer = ['yes', 'no']

@application.route('/')
def hello_world():
    return jsonify({'message' : 'Azure web api endpoint'})

@application.route('/azure')
def azure():
    random.shuffle(answer)
    return jsonify({'message' : random.choice(answer)})

if __name__ == '__main__':
    application.run()


