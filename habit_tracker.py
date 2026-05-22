from datetime import date, timedelta
import json
habits = []


def save_habits():

    with open("habits.json", "w") as file:

        json.dump(habits, file)

def load_habits():

    global habits

    try:

        with open("habits.json", "r") as file:

            habits = json.load(file)

    except FileNotFoundError:

        habits = []


load_habits()
while True:

    print("\n=== HABIT TRACKER ===")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Delete Habit")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        habit_name = input("Enter habit name: ")

        habit_data = {
            "name" : habit_name,
            "streak" : 0,
            "last_completed" : ""
        }

        habits.append(habit_data)
        save_habits()
        print("Habit added!")
        
    elif choice == "2":
        for i,habs in enumerate(habits,start=1):
            print(f" {i}. {habs['name']} | Streak: {habs['streak']} | Last Completed: {habs['last_completed']}")

    elif choice == "3":
        habit_no = int(input("Enter habit number: "))
        if 1 <= habit_no <= len(habits):

            today = date.today()
            yesterday = today - timedelta(days=1)
            last_completed = habits[habit_no - 1]["last_completed"]

            # FIRST TIME COMPLETION
            if last_completed == "":
                habits[habit_no - 1]["streak"] = 1

            else:
                last_completed_date = date.fromisoformat(last_completed)

                # ALREADY COMPLETED TODAY
                if last_completed_date == today:
                    print("Habit already completed today!")
                    continue

                # CONTINUOUS STREAK
                elif last_completed_date == yesterday:

                    habits[habit_no - 1]["streak"] += 1

                # STREAK BROKEN
                else:

                    habits[habit_no - 1]["streak"] = 1

            habits[habit_no - 1]["last_completed"] = str(today)
            save_habits()
            print("Habit completed!")

        else:

            print("Invalid habit number!")

            
    elif choice == "4":
        habit_no = int(input("Enter habit number: "))
        habits.pop(habit_no - 1)
        save_habits()
        print("Habit deleted")

    elif choice == "5":
        print("Exit")
        break

    else:
        print("Invalid option!")