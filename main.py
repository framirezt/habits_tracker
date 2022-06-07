from habit import *
from db import *
from analytics import *
import questionary


def cli():
  db = get_db()

  stop = False
  while not stop:
    choice = questionary.select("What do you want to do?",choices=["1. Create a new Habit", "2. Check off your Habit", "3. Delete a habit", "4. Get My Analytics", "5. Exit"]).ask()

    if choice == "1. Create a new Habit":
      habit_name = questionary.text("What's the name of the habit you want to create?").ask()
      periodicity = questionary.select("How often do you want to do this task?",choices=["Daily", "Weekly", "Monthly"]).ask()
      habit = Habit(habit_name, periodicity)
      habit.store_newHabit(db)
      # habit.start_periodicity()

    elif choice == "2. Check off your Habit":
      habit_name = questionary.text("What's the name of the habit you want to check-off?").ask()
      habit = Habit(habit_name, "NULL")
      habit.checkingOff(db)
    
    elif choice == "3. Delete a habit":
      habit_name = questionary.text("What's the name of the habit you want to delete?").ask()
      delete_habit(db, habit_name)
      
    elif choice == "4. Get My Analytics":
      analytics_choice = questionary.select("Which analytics do you want to see?",choices=["1. All your current habits with their details.", "2. All habits with a same periodicity", "3. The longest streak you have had out of all your habits.", "4. The longest streak for a specific habit."]).ask()
      if analytics_choice == "1. All your current habits with their details.":
        habits_list(db)
      

    else:
      print("You have exited successfully.")
      stop = True


if __name__ == '__main__':
  cli()

# python3 main.py