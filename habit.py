from db import *
import time

class Habit:

  def __init__(self, habit_name:str, periodicity:str):
    """This creates each new habit. The name and periodicity need to be defined.

    Args:
        habit_name (str): Name/description of the habit
        periodicity (str): The time-period desired to complete the task.
    """
    self.habit_name = habit_name
    self.periodicity = periodicity
    self.streak = 0
    self.checked = False
    if periodicity == "Daily": self.seconds = 24*60*60
    elif periodicity == "Weekly": self.seconds = 24*60*60*7
    elif periodicity == "Monthly": self.seconds = 4*60*60*7*4


  def incremenet(self):
    """Increases the streak by 1.
    """
    self.streak += 1
  
  def reset(self):
    """Resets streak to zero.
    """
    self.streak = 0

  def store_newHabit(self, db):
    """Stores the new habit into the defined database.

    Args:
        db (str): The database where the new habit will be stored.
    """
    new_Habit(db,self.habit_name,self.periodicity,self.streak)
  
  def checkingOff(self,db):
    """This function is used every time the user needs to check-off the habit. It increase the streak by one and inserts a new row into the habits_data table with the new data. It also updates the Habits table by getting the value of the streak and incrementing it by one.

    Args:
        db (str): The database where the new habit will be stored.
    """
    self.streak = int(self.convert_streakDB(db))
    self.incremenet()
    self.checked = True
    habit_checkingOff(db, self.habit_name, self.streak, True)
    update_streak(db,self.habit_name,self.streak)


  def set_periodicity(self):
    """This method sets the timespan for the habit. It converts the specified periodicity to seconds. Then, it go to sleep for the timespan (in seconds) and when its over, it checks if the habit has been checked-off. If its not checked-off, then the streak is reset to zero and added to the database.
    """
    time.sleep(self.seconds)
    if self.checked == True: return
    self.reset()
    db = get_db()
    self.checkingOff(db)
  
  def start_periodicity(self):
    """This starts the timespan of the habit. It runs indefinitely so the timespan is always being counted in case the user misses to check-off.
    """
    while True:
      self.set_periodicity()

  def convert_streakDB(self, db):
    """Used to get the streak from the database and then convert it to integer so it can be incremented.

    Args:
        db (str): The database where the new habit will be stored.

    Returns:
        str: The value of the streak from the database
    """
    streak_list = get_streak(db,self.habit_name)
    for streak in streak_list:
      return streak[0]






