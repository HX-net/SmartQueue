# Smart Queue — Python Practice Project

A simple queue management system built with Python that issues numbered tickets, manages waiting customers, and announces the next number using text-to-speech.

## 📌 Overview

Smart Queue is an educational project designed to practice fundamental Python programming concepts through a practical application.

The program allows users to:
- Issue new queue tickets.
- View the list of waiting numbers.
- Call the next customer in the queue.
- Announce ticket numbers using text-to-speech.
- Exit the application safely.

## ✨ Features

- **Automatic Ticket Numbering:** Assigns sequential ticket numbers starting from 50.
- **Waiting List Management:** Stores and organizes waiting numbers.
- **Voice Announcements:** Reads the next ticket number aloud.
- **Interactive Menu:** Provides a simple command-line interface.
- **Input Validation:** Handles invalid menu selections.
- **FIFO Queue:** Serves customers in the order they arrive.

## 🛠️ Technologies

- **Language:** Python
- **Library:** [pyttsx3](https://pypi.org/project/pyttsx3/)
- **Interface:** Command-Line Interface (CLI)

## 📋 Requirements

- Python 3.9 or later
- pip
- A supported text-to-speech engine and voice installed on your system

## 🚀 Installation and Usage

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-folder>
```

Replace the placeholders with your repository URL and folder name.

### 2. Install dependencies

```bash
pip install pyttsx3
```

### 3. Run the application

Save the source code as `main.py` and execute:

```bash
python main.py
```

## 🎮 Menu Options

| Option | Description |
|---|---|
| 1 | Get a new ticket |
| 2 | Show the waiting list |
| 3 | Call the next number |
| 4 | Exit the application |

## 🧠 Learning Objectives

This project helps students practice:

- Variables and data types
- Lists and list methods (`append()` and `pop()`)
- Functions and parameters
- Conditional statements (`if`, `elif`, `else`)
- Loops (`for` and `while`)
- User input and string formatting
- External Python libraries
- Text-to-speech functionality
- Exception handling (`try`, `except`, `finally`)
- Queue data structures and the FIFO principle

## 📂 Project Structure

```text
Smart-Queue/
├── main.py
└── README.md
```

## 🎯 Suggested Improvements

Students can extend the project by adding:

- Customer names alongside ticket numbers
- Total issued ticket statistics
- A feature to remove a specific ticket
- A configurable starting ticket number
- A graphical user interface (GUI)
- Persistent storage for waiting numbers

## 👨‍🏫 Educational Credit

**Practice Project**  
Taught by the **CS50x Iran Academic Team**.

This project is intended for educational purposes and helps students apply fundamental Python concepts in a practical scenario.

---

Made for learning, practicing, and building with Python. 🐍
