from db import *

# return a list of all currently tracked habits,
def habits_list(db, habit_name):
  """
  Gets the list of all the habits a user is currently tracking.
  :param db:
  :param habit_name:
  :return:
  """
  data = get_HabitData(db, habit_name)
  return len(data)


# return a list of all habits with the same periodicity,
# return the longest run streak of all defined habits,
# return the longest run streak for a given habit.