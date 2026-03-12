from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "super_secret_key" # strictly for flash messages and dev
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "database.db")

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db_connection()
    expenses = conn.execute("SELECT * FROM expenses ORDER BY date DESC, id DESC").fetchall()
    conn.close()
    
    total_spending = sum(expense["amount"] for expense in expenses)
    return render_template("index.html", expenses=expenses, total_spending=total_spending)

@app.route("/add", methods=("GET", "POST"))
def add_expense():
    if request.method == "POST":
        title = request.form.get("title")
        amount = request.form.get("amount")
        category = request.form.get("category")
        date = request.form.get("date")

        if not title or not amount or not category or not date:
            flash("All fields are required!", "error")
        else:
            try:
                amount_float = float(amount)
                conn = get_db_connection()
                conn.execute(
                    "INSERT INTO expenses (title, amount, category, date) VALUES (?, ?, ?, ?)",
                    (title, amount_float, category, date)
                )
                conn.commit()
                conn.close()
                flash("Expense added successfully!", "success")
            except ValueError:
                flash("Invalid amount entered.", "error")
            
        return redirect(url_for("index"))

    return redirect(url_for("index"))

@app.route("/delete/<int:id>", methods=("POST",))
def delete_expense(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM expenses WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    flash("Expense deleted successfully!", "success")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
