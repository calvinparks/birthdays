import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database
        inputName = request.form.get("name")
        
        if not inputName.isalnum():
            return redirect("/") 
            
        try:
            inputMonth = int(request.form.get("month"))
        except:
            return redirect("/") 
            
        try:
            inputDay = int(request.form.get("day"))
        except:
            return redirect("/")
        
        if inputDay < 1 or inputDay > 32:
            return redirect("/")
            
        if inputMonth < 1 or inputMonth > 12:
            return redirect("/")

        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", request.form.get("name"), request.form.get("month"), request.form.get("day"))
        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        rows= db.execute("select * from birthdays");
        return render_template("index.html",rows=rows )


