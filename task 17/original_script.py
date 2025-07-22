import argparse
import os
import logging

TASKS_FILE = "tasks.txt"
LOG_FILE = "log.txt"

# Configure logging
logging.basicConfig(filename=LOG_FILE, level=logging.ERROR,
                    format='%(asctime)s %(levelname)s:%(message)s')

class TaskError(Exception):
    """Custom exception for task errors."""

def load_tasks():
    try:
        if not os.path.exists(TASKS_FILE):
            return []
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        logging.error(f"Error loading tasks: {e}")
        raise TaskError("Failed to load tasks.")

def save_tasks(tasks):
    try:
        with open(TASKS_FILE, "w", encoding="utf-8") as f:
            for task in tasks:
                f.write(task + "\n")
    except Exception as e:
        logging.error(f"Error saving tasks: {e}")
        raise TaskError("Failed to save tasks.")

def add_task(task):
    try:
        tasks = load_tasks()
        tasks.append(task)
        save_tasks(tasks)
        return True
    except TaskError as e:
        print(e)
        return False

def view_tasks():
    try:
        tasks = load_tasks()
        return tasks
    except TaskError as e:
        print(e)
        return []

def delete_task(index):
    try:
        tasks = load_tasks()
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            return removed
        else:
            raise TaskError("Invalid task number.")
    except TaskError as e:
        logging.error(f"Delete error: {e}")
        print(e)
        return None

def export_tasks(filename):
    try:
        tasks = load_tasks()
        with open(filename, "w", encoding="utf-8") as f:
            for task in tasks:
                f.write(task + "\n")
        return True
    except Exception as e:
        logging.error(f"Export error: {e}")
        print("Failed to export tasks.")
        return False

def main():
    parser = argparse.ArgumentParser(description="📝 To-Do List Manager")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("view", help="View all tasks")
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", type=str, help="Task description")

    del_parser = subparsers.add_parser("delete", help="Delete a task by number")
    del_parser.add_argument("number", type=int, help="Task number to delete")

    export_parser = subparsers.add_parser("export", help="Export tasks to a .txt file")
    export_parser.add_argument("filename", type=str, help="Export filename")

    args = parser.parse_args()

    if args.command == "add":
        if add_task(args.task):
            print("Task added!")
    elif args.command == "view":
        tasks = view_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")
    elif args.command == "delete":
        removed = delete_task(args.number)
        if removed:
            print(f"Deleted: {removed}")
    elif args.command == "export":
        if export_tasks(args.filename):
            print(f"Tasks exported to {args.filename}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()