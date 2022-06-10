# HABITS TRACKER PROJECT

This application allows users to keep track of their own habits/tasks that they want to complete every certain time. It's developed using a command line interface instead of a UI. Here, users interact with the application by answering the questions asked by the CLI in order to create, delete, track and analyze their habits. All that’s needed to develop good habits.​

# Installation

To be able to run this application you must have Python installed and the following tools. Depending on your Python version the commands to install these will be different. Use the corresponding command for your version:

```shell
pip install -U pytest
pip install questionary
```

or (for Python 3.10)

```shell
pip3 install -U pytest
pip3 install questionary
```

# Starting The App

To start the application, run this command on the command line. After this, just follow the instructions on your screen. If you have questions about the usage, go to the instructions section below. The commands to start it also depend on your Python version.

```shell
python main.py
```

or (for python 3.10)

```shell
python3 main.py
```

and follow instructions on screen

# Testing

To test the application just run your corresponding command:

```shell
pytest .
```

or (for python 3.10)

```shell
python3 -m pytest
```

# Instructions Of Use

1. Start the application with the starting command
2. To create a habit, select option #1. Then name the habit and specify the period you want to repeat the habit. The name must be typed the same way every time it is used.
3. To check-off you habit after completion, select option #2 and specify the name of the habit you just completed.
4. To delete a habit you no longer want to use, select option #3 and specify the name of the habit you want to delete.
5. To analyze your habits, select option #4 and then choose one of the analytics you want to get from the options available.
6. Use option #5 every time you want to exit/stop the application.
7. Make sure you type the names of the habits correctly.
