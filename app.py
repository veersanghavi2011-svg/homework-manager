from flask import Flask, render_template, request, redirect, url_for
from Homework_manager import load_homework, homework_list, save_homework
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    load_homework()

    completed_count = 0
    incomplete_count = 0
    high_priority_count = 0

    for task in homework_list:
        if task.get("completed", False):
            completed_count += 1
        else:
            incomplete_count += 1

        if task.get("priority") == "High":
            high_priority_count += 1

    recent_homework = homework_list[-3:]

    return render_template(
        "index.html",
        homework_count=len(homework_list),
        completed_count=completed_count,
        incomplete_count=incomplete_count,
        high_priority_count=high_priority_count,
        recent_homework=recent_homework
    )

@app.route("/homework")
def homework_page():
    load_homework()

    filter_type = request.args.get("filter", "all")

    filtered_homework = []

    priority_order = {
        "High": 1,
        "Medium": 2,
        "Low": 3
    }

    for task in homework_list:

        if filter_type == "high":
            if task.get("priority") == "High":
                filtered_homework.append(task)

        elif filter_type == "completed":
            if task.get("completed", False):
                filtered_homework.append(task)

        elif filter_type == "incomplete":
            if not task.get("completed", False):
                filtered_homework.append(task)

        else:
            filtered_homework.append(task)

    filtered_homework.sort(
        key=lambda task: (
            priority_order.get(task.get("priority"), 3),
            datetime.strptime(task.get("due_date"), "%m-%d-%Y")
        )
    )

    today = datetime.now()

    for task in filtered_homework:
        due = datetime.strptime(task.get("due_date"), "%m-%d-%Y")

        if due < today and not task.get("completed", False):
            task["overdue"] = True
        else:
            task["overdue"] = False


    return render_template(
        "homework.html",
        homework=filtered_homework,
        current_filter=filter_type
    )


@app.route("/add", methods=["GET", "POST"])
def add_page():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        due_date = request.form["due_date"]
        priority = request.form["priority"]

        due_date = datetime.strptime(
            due_date,
            "%Y-%m-%d"
        ).strftime("%m-%d-%Y")

        homework_list.append({
            "name": name,
            "description": description,
            "due_date": due_date,
            "priority": priority,
            "completed": False
        })

        save_homework()

        return redirect(url_for("home"))

    return render_template("add.html")


@app.route("/complete/<name>")
def complete_homework(name):
    load_homework()

    for task in homework_list:
        if task.get("name") == name:
            task["completed"] = True
            break

    save_homework()

    return redirect(url_for("homework_page"))


@app.route("/delete/<name>")
def delete_homework(name):
    load_homework()

    global homework_list

    homework_list = [
        task for task in homework_list
        if task.get("name") != name
    ]

    save_homework()

    return redirect(url_for("homework_page"))

@app.route("/search")
def search_page():
    load_homework()

    keyword = request.args.get("q", "").lower()

    results = []

    for task in homework_list:
        if (
            keyword in task["name"].lower()
            or keyword in task["description"].lower()
        ):
            results.append(task)

    return render_template(
        "search.html",
        homework=results,
        keyword=keyword
    )



if __name__ == "__main__":
    app.run(debug=True)