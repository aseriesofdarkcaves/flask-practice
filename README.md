# flask-practice

Practice code from the book Flask Web Development by Miguel Grinberg.

## Initial setup

In the same current directory as this project:

```shell
# generate a virtual environment for this project
python3 -m venv venv

# activate the local virtual environment
source venv/bin/activate

# install flask dependency to the virtual environment
pip install flask

# check dependencies
pip freeze

# freeze the current requirements into a file
pip freeze -l > requirements.txt

# confirm flask is available within python interpreter
python
import flask

# exit virtual environment shell
deactivate
```