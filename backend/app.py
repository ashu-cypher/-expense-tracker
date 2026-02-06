from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# create / connect database
def get_db():
    conn = sqlite3.connect("expenses.db")
    conn.row_factory = sqlite3.Row
    return conn

# create table
@app.route("/init")
def init_db():
    db = get_db()
    db.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount INTEGER,
            category TEXT,
            date TEXT
        )
    """)
    db.commit()
    return "Database created"

# add expense
@app.route("/add", methods=["POST"])
def add_expense():
    data = request.json
    db = get_db()
    db.execute(
        "INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)",
        (data["amount"], data["category"], data["date"])
    )
    db.commit()
    return jsonify({"message": "Expense added"})

# get all expenses
@app.route("/expenses")
def get_expenses():
    db = get_db()
    rows = db.execute("SELECT * FROM expenses").fetchall()
    return jsonify([dict(row) for row in rows])

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)

