"""
Project: Object-Oriented To-Do List Manager
Author: Borhan Babazadeh
Date: June 2025

Description:
This Python script implements a simple To-Do list manager using object-oriented programming (OOP) principles.
The project defines two main classes — `Task` and `ToDoList` — to manage tasks with attributes such as name, description, and priority.
Users can add, remove, display, save, and load tasks from a CSV file via a user-friendly text-based menu.

This script is designed for educational purposes and demonstrates basic file handling, class design, and user interaction in Python.

License: MIT License
"""

import csv

class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority

    def to_list(self):
        return [self.name, self.description, self.priority]

    def __str__(self):
        return f"name: {self.name} | description: {self.description} | priority: {self.priority}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("task appended successfully.\n")

    def remove_task(self, name):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                print("task removed successfully\n")
                return
        print("error 404: task not found\n")

    def show_tasks(self):
        if not self.tasks:
            print("list is empty!\n")
        else:
            print("\nlist of tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
            print()

    def save_to_csv(self, filename="tasks.csv"):
        with open(filename, mode="w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "description", "priority"])
            for task in self.tasks:
                writer.writerow(task.to_list())
        print("list saved in file.\n")

    def load_from_csv(self, filename="tasks.csv"):
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                self.tasks = [Task(row["name"], row["description"], row["priority"]) for row in reader]
            print("list loaded from file.\n")
        except FileNotFoundError:
            print("error 404: file not found\n")

# منوی متنی برنامه
def show_menu():
    print("TO_DO list manager")
    print("1. append tasks")
    print("2. delete task")
    print("3. show toDo list")
    print("4. save list")
    print("5. load list")
    print("6. exit")

def main():
    todo = ToDoList()
    todo.load_from_csv()

    while True:
        show_menu()
        choice = input("your choice(1-6): ").strip()

        if choice == "1":
            name = input("task name: ")
            description = input("description: ")
            priority = input("priority (High,low,normal): ")
            task = Task(name, description, priority)
            todo.add_task(task)

        elif choice == "2":
            name = input("task name you wanna delete: ")
            todo.remove_task(name)

        elif choice == "3":
            todo.show_tasks()

        elif choice == "4":
            todo.save_to_csv()

        elif choice == "5":
            todo.load_from_csv()

        elif choice == "6":
            print("goodbye!")
            break

        else:
            print("invalid choice let's Try again\n")

if __name__ == "__main__":
    main()
