from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/users")

@app.route('/users')
def allUsers():
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users = users)

@app.route('/users/new')
def newUsers():
    return render_template("create.html")

@app.route('/addUser', methods=['post'])
def add_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

