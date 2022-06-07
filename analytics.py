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

# return a list of all habits with the same periodicity,

# return the longest run streak of all defined habits,
# return the longest run streak for a given habit.