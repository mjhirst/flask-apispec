# flask-apispec

This Python Flask application is a basic working example of using [apispec](https://github.com/marshmallow-code/apispec) to use Python's docstrings to pull out an OpenApi 3.0 specification. 
Most of the code (especially the code for the `DocPlugin`) comes from the [apispec documentation](https://apispec.readthedocs.io/en/latest/install.html) especially after some dead ends using the FlaskPlugin().

### Install and Run
```
  pipenv install --dev
  pipenv run flask run
```
Navigate to `/` root to get a print of the schema in JSON for the browser and YAML in the console.

The route `/i/<gist_id>` prints out whatever you put in `<gist_id>` but you'll see the docstring appended to the schema when at `/` root.