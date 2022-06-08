from habit import *
from db import *
from analytics import *
import questionary


def cli():
  db = get_db()

  stop = False
  while not stop:
    choice = questionary.select("What do you want to do?",
    choices=["1. Create a new Habit", 
    "2. Check off your Habit", 
    "3. Delete a habit", 
    "4. Get My Analytics", 
    "5. Exit"]).ask()

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
      analytics_choice = questionary.select("Which analytics do you want to see?",
      choices=[
        "1. All your current habits with their details.", 
        "2. All habits with a same time-period", 
        "3. The longest streak you have out of all your current habits.", 
        "4. The longest streak you've had for a specific habit.",
        "5. Get the log of all the times you've checked-off a specific habit."]).ask()
      if analytics_choice == "1. All your current habits with their details.":
        habits_list(db)
      elif analytics_choice == "2. All habits with a same time-period":
        periodicity = questionary.select("How often do you want to do this task?",choices=["Daily", "Weekly", "Monthly"]).ask()
        habits_periodicity(db, periodicity)
      elif analytics_choice == "3. The longest streak you have out of all your current habits.":
        longest_streak(db)
      elif analytics_choice == "4. The longest streak you've had for a specific habit.":
        habit_name = questionary.text("What's the name of the habit?").ask()
        habit_longest_streak(db, habit_name)
      elif analytics_choice == "5. Get the log of all the times you've checked-off a specific habit.":
        habit_name = questionary.text("What's the name of the habit?").ask()
        checkoff_log(db, habit_name)

    else:
      print("You have exited successfully.")
      stop = True


if __name__ == '__main__':
  cli()

# python3 main.py