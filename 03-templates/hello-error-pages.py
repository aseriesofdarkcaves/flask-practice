from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('base-bootstrap.html', title='Hello Bootstrap!')


@app.errorhandler(404)
def error_not_found(e):
    return render_template('error-bootstrap.html', title='HTTP-404', error_message='Not Found'), 404


@app.errorhandler(500)
def error_internal_error(e):
    return render_template('error-bootstrap.html', title='HTTP-500', error_message='Internal Error'), 500


if __name__ == '__main__':
    app.run()
