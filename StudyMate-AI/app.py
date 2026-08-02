from flask import Flask, render_template, request, redirect, session

from config import SECRET_KEY

from utils.gemini_ai import ask_gemini

from database.database import (
    create_database,
    add_user,
    check_user,
    add_task,
    get_tasks,
    delete_task
)


app = Flask(__name__)

app.secret_key = SECRET_KEY

# Create Database
create_database()



# Home Page
@app.route("/")
def home():

    return render_template("index.html")



# Register
@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]

        email = request.form["email"]

        password = request.form["password"]


        add_user(
            name,
            email,
            password
        )


        return redirect("/login")


    return render_template("register.html")





# Login
@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]

        password = request.form["password"]


        user = check_user(
            email,
            password
        )


        if user:

            session["user"] = user[1]

            return redirect("/dashboard")


        else:

            return "Invalid Email or Password"



    return render_template("login.html")





# Dashboard
@app.route("/dashboard")
def dashboard():

    if "user" not in session:

        return redirect("/login")


    return render_template(
        "dashboard.html",
        username=session["user"]
    )





# Attendance
@app.route("/attendance", methods=["GET","POST"])
def attendance():

    percentage = None


    if request.method == "POST":

        total = int(
            request.form["total"]
        )

        present = int(
            request.form["present"]
        )


        if total > 0:
            percentage = round(
                (present / total) * 100,
                2
        )
        else:
            percentage = 0


    return render_template(
        "attendance.html",
        percentage=percentage
    )





# CGPA Calculator
@app.route("/cgpa", methods=["GET","POST"])
def cgpa():

    result = None


    if request.method == "POST":

        m1 = float(request.form["marks1"])

        m2 = float(request.form["marks2"])

        m3 = float(request.form["marks3"])

        m4 = float(request.form["marks4"])


        result = round(
            (m1+m2+m3+m4)/4,
            2
        )


    return render_template(
        "cgpa.html",
        cgpa=result
    )





# Todo Manager
@app.route("/todo", methods=["GET","POST"])
def todo():

    if "user" not in session:

        return redirect("/login")


    username = session["user"]


    if request.method == "POST":

        task = request.form["task"]

        add_task(
            username,
            task
        )


    tasks = get_tasks(
        username
    )


    return render_template(
        "todo.html",
        tasks=tasks
    )





# Delete Task
@app.route("/delete_task/<int:id>")
def delete_task_route(id):

    delete_task(id)

    return redirect("/todo")





# Timer Page
@app.route("/timer")
def timer():

    if "user" not in session:
        return redirect("/login")

    return render_template("timer.html")



# Logout
@app.route("/logout")
def logout():

    session.pop(
        "user",
        None
    )

    return redirect("/login")



@app.route("/chatbot", methods=["GET","POST"])
def chatbot():

    if "user" not in session:
        return redirect("/login")

    answer = None

    if request.method == "POST":
        question = request.form["question"]
        answer = ask_gemini(question)

    return render_template(
        "chatbot.html",
        answer=answer
    )



if __name__ == "__main__":

    app.run(debug=True)