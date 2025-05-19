from flask import Flask, render_template_string, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    name = ""
    if request.method == "POST":
        name = request.form.get("name", "")
    return render_template_string("""
        <form method="post">
            <input name="name" placeholder="Введите имя">
            <input type="submit">
        </form>
        {% if name %}
        <h1>Hello, {{ name }}!</h1>
        {% endif %}
    """, name=name)
