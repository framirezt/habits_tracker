from habit import Habit
from db import *
from analytics import checkoff_log, habit_longest_streak, habits_list, longest_streak

class TestHabit:

  def setup_method(self):
    """Sets up the database and the tables that are going to be used for the tests.
    """
    self.db = get_db("test1.db")
    new_Habit(self.db, "running","daily")
    new_Habit(self.db, "sleeping","daily")
    new_Habit(self.db, "grocery shopping","weekly")
    new_Habit(self.db, "hair cut","monthly")
    new_Habit(self.db, "eating","daily")
    habit_checkingOff(self.db,"running", 1, True)
    habit_checkingOff(self.db,"sleeping", 1, True)
    habit_checkingOff(self.db,"grocery shopping", 1, True)
    habit_checkingOff(self.db,"hair cut", 1, True)
    habit_checkingOff(self.db,"eating", 1, True)
    habit_checkingOff(self.db,"eating", 2, True)

  def test_habit(self):
    """Tests the habit methods to check everything works.
    """
    habit = Habit('running', "daily")

    habit.store_newHabit(self.db)
    habit.incremenet()
    habit.checkingOff(self.db)
  
    habit.reset()
    habit.incremenet()
    habit.incremenet()

  def test_db_habit(self):
    """Tests the analytics functionality. One test per function of the analytics to check they all work as expected.
    """
    data = get_Habits(self.db, "running")
    assert len(data)==1
    count = habits_list(self.db)
    assert len(count)==5
    periodicity = get_Habits_Periodicity(self.db,"daily")
    assert len(periodicity) == 3
    log_length = checkoff_log(self.db, "eating")
    assert log_length == 2
    longestStreak = longest_streak(self.db)
    assert longestStreak == 'eating'
    longest_perHabit = habit_longest_streak(self.db,"eating")
    assert longest_perHabit == 2


  def teardown_method(self):
    """Removes the "test" database once the testing is done.
    """
    import os
    os.remove("test1.db")



# python3 -m pytest 