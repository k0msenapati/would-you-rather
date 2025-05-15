from flask import render_template
from flask_login import current_user, login_required
from models import Question

def register_main_routes(app, db):
    @app.route("/")
    def index():
        return render_template("index.html", user=current_user)

    @app.route("/dashboard")
    @login_required
    def dashboard():
        questions = Question.query.order_by(Question.created_at.desc()).all()
        return render_template("dashboard.html", questions=questions, user=current_user)
