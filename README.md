# Web-Based Expense Tracker

A simple, modern, dark-themed Expense Tracker Application built using Python Flask, HTML, Vanilla CSS, JS, and SQLite.

## Features
- Dashboard with total spending overview
- Add new expenses with categories and date
- View recent expenses in a beautifully styled table
- Delete expenses
- SQLite database for persisting records
- Clean, responsive glassmorphism dark mode UI

## Prerequisites
- Python 3.x

## How to Run Locally

1. **Clone or Download the Project.**
2. **Navigate to the project folder:**
   ```bash
   cd "d:\Nav Labs\CapstoneProjects\student-management"
   ```
3. **Create a virtual environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
4. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Initialize the SQLite database:**
   ```bash
   python init_db.py
   ```
6. **Run the Flask application:**
   ```bash
   python app.py
   ```
7. **Access the Web App:**
   Open your browser and navigate to `http://127.0.0.1:5000/`.
