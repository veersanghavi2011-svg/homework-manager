import json
from datetime import datetime

homework_list = []

priority_order = {
    "High": 1,
    "Medium": 2,
    "Low": 3
}

def sort_homework(homework):
    return (
        priority_order.get(homework.get("priority", "Low"), 3),
        datetime.strptime(homework.get("due_date", "01-01-1900"), "%m-%d-%Y")
    )


def add_homework():
    homework = input("Enter homework: ")
    description = input("Enter description: ")

    while True:
        try:
            due_date = input("Enter due date (MM-DD-YYYY): ")
            datetime.strptime(due_date, "%m-%d-%Y")
            break
        except ValueError:
            print("Invalid date format. Please enter the date in MM-DD-YYYY format.")

    priority = input("Enter priority (High/Medium/Low): ").capitalize()

    while priority not in ["High", "Medium", "Low"]:
        print("Invalid priority. Please enter High, Medium, or Low.")
        priority = input("Enter priority (High/Medium/Low): ").capitalize()

    homework_list.append({
        "name": homework,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "completed": False
    })

    save_homework()
    print("Homework added!")


def view_homework():
    if len(homework_list) == 0:
        print("No homework found!")
        return

    print("Your Homework:")

    sorted_homework = sorted(
    homework_list,
    key=sort_homework
)

    for homework in sorted_homework:
        print("| Name:", homework["name"])
        print("| Description:", homework["description"])
        print("| Due Date:", homework["due_date"])
        print("| Priority:", homework.get("priority", "Not Set"))
        print("| Status:", "Completed" if homework["completed"] else "Not Completed")
        print()


def search_homework():
    keyword = input("Enter keyword to search: ").lower()

    found = False

    for homework in homework_list:
        if keyword in homework["name"].lower() or keyword in homework["description"].lower():
            print()
            print("| Name:", homework["name"])
            print("| Description:", homework["description"])
            print("| Due Date:", homework["due_date"])
            print("| Priority:", homework.get("priority", "Not Set"))
            print("| Status:", "Completed" if homework["completed"] else "Not Completed")
            found = True

    if not found:
        print("No matching homework found.")

def delete_homework():
    if len(homework_list) == 0:
        print("No homework to delete!")
        return

    print("Your Homework:")

    for index, homework in enumerate(homework_list):
        print(index + 1, "Name:", homework["name"])

    try:
        choice = int(input("Which homework do you want to delete? "))
    except ValueError:
        print("Please enter a number.")
        return

    if 1 <= choice <= len(homework_list):
        homework_list.pop(choice - 1)
        save_homework()
        print("Homework deleted!")
    else:
        print("Invalid homework number.")


def complete_homework():
    if len(homework_list) == 0:
        print("No homework to complete!")
        return

    print("Your Homework:")

    for index, homework in enumerate(homework_list):
        print(index + 1, "Name:", homework["name"])

    try:
        choice = int(input("Which homework do you want to mark as completed? "))
    except ValueError:
        print("Please enter a number.")
        return

    if 1 <= choice <= len(homework_list):
        homework_list[choice - 1]["completed"] = True
        save_homework()
        print("Homework marked as completed!")
    else:
        print("Invalid homework number.")



def save_homework():
    with open("tasks.json", "w") as file:
        json.dump(homework_list, file, indent=4)


def load_homework():
    global homework_list

    try:
        with open("tasks.json", "r") as file:
            homework_list = json.load(file)

    except FileNotFoundError:
        homework_list = []


load_homework()

if __name__ == "__main__":
    while True:
        print("===== Homework Manager =====")
        print("1. Add Homework")
        print("2. View Homework")
        print("3. Delete Homework")
        print("4. Mark Homework as Completed")
        print("5. Search Homework")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_homework()

        elif choice == "2":
            view_homework()

        elif choice == "3":
            delete_homework()

        elif choice == "4":
            complete_homework()

        elif choice == "5":
            search_homework()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid option.")