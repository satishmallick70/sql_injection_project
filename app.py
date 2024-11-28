from flask import Flask, request,render_template
import sqlite3

app=Flask(__name__)

# Route for the login page
@app.route("/", methods=["GET", "POST"])
def login():
  if request.method =="POST":
     username = request.form["username"]  # Get input from the user
     password = request.form["password"]

     # Vulnerable SQL query
     query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
     conn = sqlite3.connect("testdb.db")
     cursor = conn.cursor()
     cursor.execute(query)
     user = cursor.fetchone()  # Fetch the first matching row
     conn.close()

     if user:  # If a matching row is found, login succeeds
            return "Login successful!"
     else:
            return "Invalid username or password!"

       # Render the login form
  return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)

