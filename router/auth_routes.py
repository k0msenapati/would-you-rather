from flask import render_template, request, redirect, flash, url_for
from flask_login import login_user, logout_user, current_user, login_required
from models import User
from sqlalchemy.exc import IntegrityError

def register_auth_routes(app, db, bcrypt):
    @app.route("/login", methods=["GET", "POST"])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for("dashboard"))
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            user = User.query.filter_by(username=username).first()
            if user and bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for("dashboard"))
            flash("Invalid username or password")
        return render_template("login.html")

    @app.route("/signup", methods=["GET", "POST"])
    def signup():
        if current_user.is_authenticated:
            return redirect(url_for("dashboard"))
        if request.method == "POST":
            username = request.form["username"]
            name = request.form["name"]
            password = request.form["password"]
            email = request.form["email"]
            hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
            new_user = User(
                name=name, username=username, email=email, password=hashed_password # type: ignore
            )
            try:
                db.session.add(new_user)
                db.session.commit()
                flash("Account created successfully! Please log in.")
                return redirect(url_for("login"))
            except IntegrityError:
                db.session.rollback()
                flash("Username or email already exists")
        return render_template("signup.html")

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        flash("You have been logged out.")
        return redirect(url_for("index"))
