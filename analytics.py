from db import *

# return a list of all currently tracked habits,
def habits_list(db, ):
  """
  Gets the list of all the habits a user is currently tracking.
  :param db:
  :param habit_name:
  :return:
  """
  list = get_AllHabits(db)
  print("\n")
  print(f"You currently have {len(list)} habits:")
  print("\n")
  for habit in list:
    print(f"----- {habit[0]} -----")
    print(f"Period: {habit[1]}")
    print(f"Streak: {habit[2]}")
    print(f"Creation  date: {habit[3]}")
    print("\n")
  return list  
  

# return a list of all habits with a same given periodicity,
def habits_periodicity(db, periodicity):
  list = get_Habits_Periodicity(db, periodicity)
  print("\n")
  print(f"You currently have {len(list)} habits with the `{periodicity}` period:")
  print("\n")
  for habit in list:
    print(f"----- {habit[0]} -----")
    print(f"Period: {habit[1]}")
    print(f"Streak: {habit[2]}")
    print(f"Creation  date: {habit[3]}")
    print("\n")
  

# return the longest run streak of all defined habits,
def longest_streak(db,):
  list = get_longest_streak(db, )
  print("\n")
  print(f"Your habit with the longest streak is:")
  print("\n")
  for habit in list:
    print(f"----- {habit[0]} -----")
    print(f"Period: {habit[1]}")
    print(f"Streak: {habit[2]}")
    print(f"Creation  date: {habit[3]}")
    print("\n")
  return habit[0]

# return the longest run streak a given habit has had since created.
def habit_longest_streak(db,habit_name):
  list = get_longest_habit_streak(db, habit_name)  
  for habit in list:
    print("\n")
    print(f"Your longest streak for '{habit[0]}' is {habit[2]}, which was completed on {habit[1]}.")
    print("\n")
  return habit[2]

    

#return a log of all check-offs for a given habit
def checkoff_log(db, habit_name):
  list = get_Habit_checkOffs(db, habit_name)
  print("\n")
  print(f"You have checked-off this habit {len(list)} times since created:")
  print("\n")
  for habit in list:
    print("------------------------------------------------------------------------------")
    print(f"|| {habit[0]} || Date: {habit[1]}  ||  streak:  {habit[2]}  ||  Checked: {habit[3]}  ||")
    
  print("------------------------------------------------------------------------------")
  print("\n")
  return len(list)


