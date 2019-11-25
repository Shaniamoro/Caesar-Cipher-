from flask import Flask, render_template, request
from keyed_caesar import KeyCaesar

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        key = request.form.get("user-key", "")
        message = request.form.get("user-message", "")
        val = request.form.get("user-val", "")

        new_message = KeyCaesar()
        result_message = new_message.run_cipher(key, message, val)

        return render_template("index.html", result_message=result_message)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
