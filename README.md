# NoxTask Manager 📝

A simple Task Management System built with Python.

NoxTask Manager is a command-line application (CLI) that allows users to create, manage, search, and organize their tasks.

Tasks are stored permanently using a JSON file.

---

## 📌 Features

- ✅ Add new tasks
- ✅ Remove tasks
- ✅ Show all tasks
- ✅ Search for tasks
- ✅ Count total tasks
- ✅ Clear all tasks
- ✅ Store tasks permanently using JSON
- ✅ Basic input error handling

---

## 🛠️ Technologies Used

- Python 3
- JSON
- File Handling

---

## 📂 Project Structure

```
NoxTask-Manager/
│
├── main.py
├── tasks.json
└── README.md
```

---

## ⚙️ How It Works

The program uses a JSON file to save tasks.

When the user:
- Adds a task
- Removes a task
- Clears tasks

The changes are automatically saved inside `tasks.json`.

Example:

```json
[
    "Learn Python",
    "Study Cybersecurity",
    "Read Book"
]
```

---

## 🚀 How To Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/NoxTask-Manager.git
```

### 2. Open the project folder

```bash
cd NoxTask-Manager
```

### 3. Run the program

```bash
python main.py
```

---

## 🖥️ Example

```
================================================
             NoxTask Manager
================================================

1) Add Task
2) Remove Task
3) Show Tasks
4) Search Task
5) Count Tasks
6) Clear Tasks
7) Exit

To choose:
```

---

## 📚 Concepts Practiced

This project helped me practice:

- Python Functions
- Lists
- Loops
- Conditional Statements
- User Input Handling
- File Handling
- JSON Data Storage
- Error Handling
- Code Organization

---

## 🔮 Future Improvements

- [ ] Add task priority (High / Medium / Low)
- [ ] Add task status (Done / Not Done)
- [ ] Add edit task feature
- [ ] Add task creation date
- [ ] Add automatic file creation if `tasks.json` does not exist
- [ ] Use Object-Oriented Programming (OOP)
- [ ] Create a graphical interface (GUI)
- [ ] Add database support

---

## 👤 Author

**Nox Hunt**

Python Beginner Developer

Learning Python & Cybersecurity 🚀