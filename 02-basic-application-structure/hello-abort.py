from flask import Flask
from flask import abort

app = Flask(__name__)

valid_users = [
    "dave",
    "eileen",
    "franchesca",
    "gerry"
]


@app.route('/')
def index():
    return '<h1>Navigate to user/name for this example!</h2>'


@app.route('/user/<name>')
def greet_user(name):
    user = find_user(name)
    if not user:
        abort(404)
    return '<h1>Hello {}!</h1>'.format(user)


def find_user(name):
    for user in valid_users:
        if user == name:
            return name
    return None


if __name__ == '__main__':
    app.run()
