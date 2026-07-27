from datetime import datetime


def suggest_priority(description, due_date):
    """
    Returns an AI priority suggestion and explanation.
    """

    today = datetime.now()

    due = datetime.strptime(
        due_date,
        "%m-%d-%Y"
    )

    days_left = (due - today).days

    description = description.lower()


    urgent_words = [
        "test",
        "exam",
        "project",
        "final",
        "quiz"
    ]


    for word in urgent_words:
        if word in description:
            return {
                "priority": "High",
                "reason": f"Your homework contains '{word}', which usually needs extra preparation."
            }


    if days_left <= 2:
        return {
            "priority": "High",
            "reason": "The due date is very close."
        }


    elif days_left <= 7:
        return {
            "priority": "Medium",
            "reason": "The assignment is due within a week."
        }


    else:
        return {
            "priority": "Low",
            "reason": "You have plenty of time before the due date."
        }



def create_study_plan(description, due_date):
    """
    Creates a simple AI study plan based on the deadline.
    """

    today = datetime.now()

    due = datetime.strptime(
        due_date,
        "%m-%d-%Y"
    )

    days_left = (due - today).days


    if days_left <= 1:

        return [
            "Review the most important concepts",
            "Complete practice problems",
            "Do a final review before submitting"
        ]


    elif days_left <= 3:

        return [
            "Break the assignment into smaller parts",
            "Complete half of the work",
            "Review and finish the remaining tasks"
        ]


    else:

        return [
            "Day 1: Read and understand the material",
            "Day 2: Work on the assignment",
            "Day 3: Review your work and make improvements"
        ]