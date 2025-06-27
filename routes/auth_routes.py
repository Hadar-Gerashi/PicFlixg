# routes/auth_routes.py
import re
import bcrypt
from flask import Blueprint, render_template, session, request, redirect, flash
from models.user import create_user, is_email_registered, read_user_by_email
from models.categories import read_categories, create_user_categories

auth_bp = Blueprint('auth_bq', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    email = ''

    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')

        errors = []

        if not email:
            errors.append("Email is required.")
        elif not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
            errors.append("Invalid email address.")

        if not password:
            errors.append("Password is required.")
        elif not re.fullmatch(r"^(?=.*[A-Za-z])(?=.*\d).{8,}$", password):
            errors.append("Password must be at least 8 characters long and include at least one letter and one number.")

        if not errors:
            user = read_user_by_email(email)
            if user:
                hashed = user['password_user'].encode("utf-8")
                if bcrypt.checkpw(password.encode("utf-8"), hashed):
                    session.permanent = True
                    session['username'] = user['users_name']
                    session['user_id'] = user['id']

                    return redirect('/home')
                else:
                    errors.append("Incorrect password.")
            else:
                errors.append("No user found with this email.")

        for error in errors:
            flash(error, "error")

        return render_template("login.html", email=email)

    return render_template("login.html", email=email)


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/home')


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    categories = read_categories()

    if request.method == 'POST':
        first_name = request.form.get('first_name', '').strip()
        last_name = request.form.get('last_name', '').strip()
        full_name = f"{first_name} {last_name}".strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')

        selected_categories = request.form.getlist('category_id[]')

        errors = []

        if not first_name:
            errors.append("First name is required.")
        elif not re.fullmatch(r"[A-Za-zא-ת]{2,}", first_name):
            errors.append("First name must contain at least 2 letters.")

        if not last_name:
            errors.append("Last name is required.")
        elif not re.fullmatch(r"[A-Za-zא-ת]{2,}", last_name):
            errors.append("Last name must contain at least 2 letters.")

        if not email:
            errors.append("Email is required.")
        elif not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
            errors.append("Invalid email address.")

        if not password:
            errors.append("Password is required.")
        elif not re.fullmatch(r"^(?=.*[A-Za-z])(?=.*\d).{8,}$", password):
            errors.append("Password must be at least 8 characters long and include at least one letter and one number.")

        if is_email_registered(email):
            errors.append("This email is already registered.")

        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('signup.html',
                                   first_name=first_name,
                                   last_name=last_name,
                                   email=email,
                                   categories=categories,
                                   selected_categories=selected_categories)

        create_user(password, email, full_name)
        user = read_user_by_email(email)
        user_id = user["id"]

        create_user_categories(user_id, selected_categories)

        session['username'] = user["users_name"]
        session['user_id'] = user_id
        return redirect('/home')

    return render_template("signup.html", categories=categories, selected_categories=[])
