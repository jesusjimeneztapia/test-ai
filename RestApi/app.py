from flask import Flask
from flask_cors import CORS

from controller import book_controller
from common import *

app = Flask(__name__)
cors = CORS(app, resources={r'/api/*': {'origins': '*'}})

@app.route('/')
def hello_world():
    return 'Welcome to my first rest api.'


book_controller.get_instance(app)

if __name__ == '__main__':
    app.run(debug=True, port=PORT)