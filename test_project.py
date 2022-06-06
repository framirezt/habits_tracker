from habit import Habit
from db import *
from analytics import habits_list

class TestHabit:

  def setup_method(self):
    self.db = get_db("test1.db")
    new_Habit(self.db, "running","daily")
    habit_checkingOff(self.db,"running", 1, True)

  def test_habit(self):
    habit = Habit('running', "daily")

    habit.store_newHabit(self.db)
    habit.incremenet()
    habit.checkingOff(self.db)
  
    habit.reset()
    habit.incremenet()
    habit.incremenet()

  def test_db_habit(self):
    data = get_Habits(self.db, "running")
    assert len(data)==1
    count = habits_list(self.db, "running")
    assert count==1


  def teardown_method(self):
    import os
    os.remove("test1.db")



# python3 -m pytest