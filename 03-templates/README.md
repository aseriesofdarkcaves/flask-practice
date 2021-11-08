# Chapter 3: Templates

Templates allow the decoupling of business and presentation logic. Flask uses the `jinga2` templating engine to render
them.

Importing the function `render_template` allows us to template a response.

Templates must exist within a directory called `templates`.

---

## hello-templates.py

Implementation of index and dynamic URL functions which use templates in the response.

---

## Flask-Bootstrap

Bootstrap is an open-source web-browser framework from Twitter which provides interface components. It is a client-side
framework, so the server only needs to provide HTML responses that reference Bootstrap's CSS and JavaScript files. This
can be done via templates.

We use a Flask extension called `flask-bootstrap` to organise the changes to the templates.

To install `flask-bootstrap` in the virtual invironment:

```shell
pip install flask-bootstrap
```

---

## hello-bootstrap.py

A simple app which uses Flask-Bootstrap. The `user-bootstrap.html` template file shows how template inheritance works by
referencing `bootstrap/base.html` from Flask-Bootstrap.

## hello-error-pages.py

Shows how to use template inheritance and how to customise error pages using decorators.
