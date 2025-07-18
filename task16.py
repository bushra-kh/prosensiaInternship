import argparse
import os
from colorama import init, Fore, Style

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(Fore.GREEN + "Task added!" + Style.RESET_ALL)

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print(Fore.YELLOW + "No tasks found." + Style.RESET_ALL)
        return
    print(Fore.CYAN + "Your To-Do List:" + Style.RESET_ALL)
    for idx, task in enumerate(tasks, 1):
        print(f"{Fore.BLUE}{idx}.{Style.RESET_ALL} {task}")

def delete_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(Fore.RED + f"Deleted: {removed}" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "Invalid task number." + Style.RESET_ALL)

def export_tasks(filename):
    tasks = load_tasks()
    with open(filename, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")
    print(Fore.GREEN + f"Tasks exported to {filename}" + Style.RESET_ALL)

def main():
    init(autoreset=True)
    parser = argparse.ArgumentParser(
        description="📝 Simple To-Do List Manager",
        epilog="Example: python task16.py add 'Buy milk'"
    )
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
        add_task(args.task)
    elif args.command == "view":
        view_tasks()
    elif args.command == "delete":
        delete_task(args.number)
    elif args.command == "export":
        export_tasks(args.filename)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()