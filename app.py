from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

# Path to CSV file
CSV_FILE = "students.csv"

# Create CSV file with header if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Email", "Age", "Course"])

@app.route("/")
def home():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form["studentName"]
    email = request.form["email"]
    age = request.form["age"]
    course = request.form["course"]

    # Save data into CSV
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, email, age, course])

    return f"""
    <h2>✅ Registration Successful!</h2>
    <p><b>Name:</b> {name}</p>
    <p><b>Email:</b> {email}</p>
    <p><b>Age:</b> {age}</p>
    <p><b>Course:</b> {course}</p>
    <p>Data saved to <b>{CSV_FILE}</b> 📁</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
