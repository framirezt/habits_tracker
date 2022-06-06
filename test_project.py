from habit import Habit

class TestHabit:

  def test_habit(self):
    habit = Habit('running', "daily")

    habit.incremenet()
    habit.reset()
    habit.incremenet()
    habit.incremenet()


# python3 -m pytest
# testing 3:43