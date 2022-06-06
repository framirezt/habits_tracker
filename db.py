import sqlite3
from datetime import date

def get_db(name="main.db"):
  db = sqlite3.connect(name)
  create_tables(db)
  return db

def create_tables(db):
  cur = db.cursor()
  
  cur.execute('''CREATE TABLE IF NOT EXISTS habits (
    habit_name TEXT PRIMARY KEY,
    periodicity TEXT
    streak INT,
    creation_date TEXT
  )''')

  cur.execute('''CREATE TABLE IF NOT EXISTS habits_data (
    habit_name TEXT,
    time_at_completion TEXT,
    current_streak INT,
    checkedOff BOOL,
    FOREIGN KEY (habit_name) REFERENCES habits(habit_name)
  )''')

  db.commit()

def new_Habit(db, name, periodicity,streak=0):
  cur = db.cursor()
  creation_date = date.today()
  cur.execute("INSERT INTO habits VALUES (?,?,?,?)", (name,periodicity,streak, creation_date))
  
  db.commit()

def habit_checkingOff(db,habit_name,streak=0,checked= False):
  cur = db.cursor()
  checking_date = date.today()
  cur.execute("INSERT INTO habits_data VALUES (?,?,?)", (habit_name,checking_date,streak, checked))
  db.commit()

#getting data from DB
def get_HabitData(db, habit_name):
  cur = db.cursor()
  cur.execute("SELECT * FROM habits_data WHERE habit_name=?", (habit_name))
  return cur.fetchall()

def get_Habits(db, habit_name):
  cur = db.cursor()
  cur.execute("SELECT * FROM habits_data WHERE habit_name=?", (habit_name))
  return cur.fetchall()
