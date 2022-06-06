from habit import *
from db import *
from analytics import *
import questionary


def cli():
  db = get_db()
  questionary.confirm("are you ready?").ask()

  stop = False
  while not stop:
    choice = questionary.select("What do you want to do?",choices=["1. Create a new Habit", "2. Check off your Habit", "3. Get My Analytics", "4. Exit"]).ask()

    if choice == "1. Create a new Habit":
      habit_name = questionary.text("What's the name of the habit you want to create?").ask()
      periodicity = questionary.select("How often do you want to do this task?",choices=["Daily", "Weekly", "Monthly"]).ask()
      habit = Habit(habit_name, periodicity)
      habit.store_newHabit(db)

    elif choice == "2. Check off your Habit":
      habit_name = questionary.text("What's the name of the habit you want to check-off?").ask()
      habit = Habit(habit_name, "NULL")
      habit.incremenet()
      habit.checkingOff(db)
      
    elif choice == "3. Get My Analytics":
      #ask if wants analytics for all or just one habit
      habit_name = questionary.text("What's the name of the habit?").ask()
      habits_count = habits_list(db, habit_name)
      print(f"You currently have {habits_count} habits.")

    else:
      print("You have exited successfully.")
      stop = True


if __name__ == '__main__':
  cli()