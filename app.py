from flask import Flask, render_template
from Homework_manager import load_homework, homework_list

app = Flask(__name__)

@app.route("/")
def home():
    load_homework()

    return render_template(
    "index.html",
    homework=homework_list,
    homework_count=len(homework_list)
)

if __name__ == "__main__":
    app.run(debug=True)