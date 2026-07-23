from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Veer's Homework Manager</h1>
    <p>My first Flask website!</p>
    """

if __name__ == "__main__":
    app.run(debug=True)