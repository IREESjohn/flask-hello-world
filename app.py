from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template(
        'helloworld.html',
        JINJA_TEMPLATE_EXAMPLE="<p>This is a fast example!</p>"
        )

@app.route("/goodbye")
def goodbye_world():
    return render_template(
        'helloworld.html',
        JINJA_TEMPLATE_EXAMPLE="<p>Goodbye Now!</p>"
        )