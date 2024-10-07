from flask import Flask
from apispec import APISpec
from docplugin import DocPlugin

app = Flask(__name__)

spec = APISpec(
    title="Gisty",
    version="1.0.0",
    openapi_version="3.0.2",
    info=dict(description="A minimal gist API"),
    plugins=[DocPlugin()],
)

spec.components.schema(
    "Gist",
    {
        "properties": {
            "id": {"type": "integer", "format": "int64"}
        }
    },
)


@app.route('/')
def root():  # put application's code here
    print(spec.to_yaml())
    return spec.to_dict()


@app.route("/i/<gist_id>")
def gist_detail(gist_id):
    """Gist detail view.

    ---
    get:
      parameters:
        - name: gist_id
          in: path
          description: ID of gist
          required: true
          schema: Gist/properties/id
      responses:
        200:
          description: Gist details
          content:
            application/json:
              schema: Gist
    """
    return "details about gist {}".format(gist_id)

# Since path inspects the view and its route,
# we need to be in a Flask request context
with app.test_request_context():
    spec.path(path="/i/{gist_id}", func=gist_detail)

if __name__ == '__main__':
    app.run()