from db import *
import time

class Habit:

  def __init__(self, habit_name:str, periodicity:str):
    self.habit_name = habit_name
    self.periodicity = periodicity
    self.streak = 0
    self.checked = False
    if periodicity == "Daily": self.seconds = 24*60*60
    elif periodicity == "Weekly": self.seconds = 24*60*60*7
    elif periodicity == "Monthly": self.seconds = 4*60*60*7*4


  def incremenet(self):
    self.streak += 1
  
  def reset(self):
    self.streak = 0

  def store_newHabit(self, db):
    new_Habit(db,self.habit_name,self.periodicity,self.streak)
  
  def checkingOff(self,db):
    self.streak = int(self.convert_streakDB(db))
    self.incremenet()
    self.checked = True
    habit_checkingOff(db, self.habit_name, self.streak, True)
    update_streak(db,self.habit_name,self.streak)


  def set_periodicity(self):
    time.sleep(self.seconds)
    if self.checked == True: return
    self.reset()
    db = get_db()
    self.checkingOff(db)
  
  def start_periodicity(self):
    while True:
      self.set_periodicity()

  def convert_streakDB(self, db):
    streak_list = get_streak(db,self.habit_name)
    for streak in streak_list:
      return streak[0]






