from db import *

class Habit:

  def __init__(self, habit_name:str, periodicity:str):
    self.habit_name = habit_name
    self.periodicity = periodicity
    self.streak = 0

  def incremenet(self):
    self.streak =+ 1
  
  def reset(self):
    self.streak = 0

  def store_newHabit(self, db):
    new_Habit(db,self.habit_name,self.periodicity,self.streak)
  
  def checkingOff(self,db):
    habit_checkingOff(db, self.habit_name, self.streak, True)




# habit = Habit('running', 'daily')
# print(habit)