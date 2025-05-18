from flask import Flask, render_template_string

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template_string("""
        <form method="post">
            <input name="name">
            <input type="submit">
        </form>
    """)
