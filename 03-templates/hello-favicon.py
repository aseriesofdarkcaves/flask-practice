from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('favicon.html', title='Hello Favicon!')


if __name__ == '__main__':
    app.run()
