"""
app.py module runs the to-do list application.
"""

import argparse
from task_manager import TaskManager

def main():
    """Main function creates arguments for application and ties them to task_manager functions."""
    parser = argparse.ArgumentParser(description='To-Do List Application')
    parser.add_argument('--add', metavar='TASK', type=str, help='Add a new task')
    parser.add_argument('--view', action='store_true', help='View all tasks')
    parser.add_argument('--delete', metavar='INDEX', type=int, help='Delete a task by its index')
    parser.add_argument('--complete', metavar='INDEX', type=int, help='Mark a task as completed')
    args = parser.parse_args()

    manager = TaskManager()

    if args.add:
        manager.add_task(args.add)
    elif args.view:
        manager.view_tasks()
    elif args.delete is not None:
        manager.delete_task(args.delete - 1)  # Adjust for zero-based index
    elif args.complete is not None:
        manager.complete_task(args.complete - 1)  # Adjust for zero-based index
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
