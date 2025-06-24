# 📝 Object-Oriented To-Do List Manager

A simple command-line To-Do list application written in Python using object-oriented programming (OOP) principles.

---

## 🔍 Project Description

This project is a **To-Do List Manager** developed in Python that demonstrates key programming concepts such as object-oriented programming (OOP), file handling with CSV, and structured data management.

The application allows users to interactively manage their tasks through a simple text-based menu. It supports adding, removing, displaying, saving, and loading tasks from a CSV file.

---

## 🧠 Problem Statement

You are tasked with building a **To-Do List Manager** that incorporates:

- Object-Oriented Programming (OOP)
- Reading from and writing to CSV files
- Basic data storage and retrieval mechanisms

---

## 📌 Key Features

- ✅ **Add New Task**: Add a task with a name, description, and priority.
- ❌ **Remove Task**: Delete a task from the list by its name.
- 📋 **View Tasks**: Display all current tasks in a readable format.
- 💾 **Save to CSV**: Automatically store all tasks in a CSV file.
- 📂 **Load from CSV**: Load task list from CSV at startup or manually.
- 🔺 **Set Priority**: Each task can be assigned a priority such as `High`, `Normal`, or `Low`.

---

## 🧱 Project Structure

### 🔸 `Task` Class
Models a single task. Each task includes:
- Task name
- Description
- Priority level

### 🔸 `ToDoList` Class
Handles management of all tasks:
- Add tasks to the list
- Remove tasks from the list
- Display all tasks
- Save/load the list to/from a CSV file

### 🔸 Menu System
A simple command-line interface that allows the user to:
- Add a new task
- Delete an existing task
- View all tasks
- Save the task list
- Load tasks from a file
- Exit the application

---

## 🛠 Technologies Used

- Python 3.x
- Standard libraries: `csv`

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3 installed:

```bash
python --version
