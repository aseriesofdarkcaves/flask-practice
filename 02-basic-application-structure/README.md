# Chapter 2: Basic Application Structure

You can run the applications via the command-line like this

```shell
export FLASK_APP=hello.py
flask run
```

In most cases, I just added the `app.run()` statement so that I can run it in PyCharm.

## hello.py

The hello world app with a single route.

## hello-dynamic.py

Builds on `hello.py` to add a second route which handles dynamic URLs.

## hello-dynamic-debug.py

Shows how to use activate the debug mode that allows viewing of stack-traces in the browser. This can also be set via
the commandline:

```shell
export FLASK_DEBUG=1
```

The console will print out a PIN to use to gain access.