import json

homework_list = []

def add_homework():
    homework = input("Enter homework: ")
    description = input("Enter description: ")
    due_date = input("Enter due date (DD-MM-YYYY): ")

    homework_list.append({
        "name": homework,
        "description": description,
        "due_date": due_date,
        "completed": False
    })

    save_homework()
    print("Homework added!")


def view_homework():
    if len(homework_list) == 0:
        print("No homework found!")
    else:
        print("Your Homework:")

        for homework in homework_list:
            print("|Name:", homework["name"])
            print("| Description:", homework["description"])
            print("| Due Date:", homework["due_date"])
            print("| Status:", "Completed" if homework["completed"] else "Not Completed")
            print()


def delete_homework():
    if len(homework_list) == 0:
        print("No homework to delete!")

    else:
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

    else:
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

while True:
    print("===== Homework Manager =====")
    print("1. Add Homework")
    print("2. View Homework")
    print("3. Delete Homework")
    print("4. Mark Homework as Completed")
    print("5. Exit")

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
        print("Exiting...")
        break

    else:
        print("Invalid option.")