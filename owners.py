"""

File: owners.py
Responsibility: Landlord Authentication (Signup & Login)
Team Member Assigned: Bibin Rufaz L

Description:
    Contains all backend routes and logic for landlord registration and login.
    Handles password hashing and sets user session variables upon successful login.

"""

from database import landlord_collection,properties_collection
from flask import Flask, render_template, url_for, request, redirect,session

def init_signup_route(app):
    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            name = request.form.get('name')
            user_id = request.form.get('user_id')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm_password')

            if name and user_id and password and confirm_password:
                existing_landlord = landlord_collection.find_one({"user_id": user_id})
                if existing_landlord:
                    return 'Landlord Already Exists.'

                if password != confirm_password:
                    return "Password doesn't match"

                landlord_data = {
                    "name": name,
                    'user_id': user_id,
                    'password': password
                }

                landlord_collection.insert_one(landlord_data)
                return redirect(url_for('login'))
            
            return 'Please fill in all the fields'
        
        return render_template('signup.html')

def init_login_route(app):
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            user_id = request.form.get('user_id')
            password = request.form.get('user_password')

            if user_id and password:
                check_user = landlord_collection.find_one({'user_id': user_id, "password": password})
                if check_user:
                    session['user_id'] = check_user['user_id']
                    session['user_name'] = check_user['name']
                    return redirect(url_for('dashboard'))
                else:
                    return 'Invalid User ID or Password'
            
            return 'Please fill all fields'
        
        return render_template('login.html')

    @app.route('/dashboard')
    def dashboard():
        if 'user_id' not in session:
            return redirect('/login')

        current_user_id = session['user_id']
        user_name = session['user_name']

        user_properties = list(properties_collection.find({
            'owner_id':current_user_id
        }))

        return render_template('dashboard.html',name=user_name,properties=user_properties)