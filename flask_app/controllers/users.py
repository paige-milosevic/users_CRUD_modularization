
from dataclasses import dataclass
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.users import User

@app.route('/')
def index():
    return render_template('menu.html')

@app.route('/viewusers')
def allUsers():
    return render_template('viewusers.html',users=User.getAll())

@app.route('/add_user')
def showForm():
    return render_template('adduser.html')

@app.route('/add_user', methods=['POST'])
def save():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    User.addUser(data)
    return redirect('/viewusers')

@app.route('/view_user/<int:id>')
def viewUser(id):
    data = {
        "id": id
    }
    return render_template('userprofile.html', user=User.getOne(data))

@app.route('/user/update', methods=['POST'])
def update():
    User.updateUser(request.form)
    return redirect('/viewusers')

@app.route('/update_user/<int:id>')
def editUser(id):
    data = {
        "id": id
    }
    return render_template("edituser.html",user=User.getOne(data))

@app.route('/user/delete/<int:id>')
def delete(id):
    data = {
        "id": id
    }
    User.remove(data)
    return redirect('/viewusers')