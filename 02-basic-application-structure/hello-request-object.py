from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return request.headers.__str__()


if __name__ == '__main__':
    app.run()
