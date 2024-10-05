# TO-DO CLI
This is an app that allows you to keep track of your TO-DOs through simple commands.

You only need Python3 to run the code.

```bash python app.py usage: app.py [-h] [--add TASK] [--view] [--delete INDEX]

To-Do List Application

options: -h, --help show this help message and exit --add TASK Add a new task --view View all tasks --delete INDEX Delete a task by its index

Example: 

$ python app.py --add "finish homework" # add a task to do
$ python app.py --view # see that it was saved
Task 1: finish homework
$ python app.py --complete 1 # mark the task as completed
$ python app.py --view # see that it was completed
Task 1: finish homework - COMPLETED
$ python app.py --delete 1 # delete the task
$ python app.py --view # confirm that task was deleted
$ python app.py --add "task 1"
$ python app.py --add "task 2"
$ python app.py --reverse #reverse the task order

Features: 

Add a Task: Easily add new tasks. 
View Tasks: Get a list of all your tasks.
Delete a Task: Remove tasks that are no longer needed.
Complete a Task: Mark tasks as completed.
Reverse a Task: Reverses task list
Team
Student A - Aune Mitchell, Student B - Psy Cisneros
