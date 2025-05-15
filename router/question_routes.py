from flask import render_template, request, redirect, flash, url_for
from flask_login import current_user, login_required
from models import Question, Answer
from datetime import datetime

def register_question_routes(app, db):
    @app.route("/create_question", methods=["GET", "POST"])
    @login_required
    def create_question():
        if request.method == "POST":
            text_a = request.form["text_a"]
            text_b = request.form["text_b"]
            categories_str = request.form.get("categories", "")

            categories = [cat.strip() for cat in categories_str.split(",") if cat.strip()]

            today = datetime.utcnow().date()
            users_questions_today = Question.query.filter(
                Question.author == current_user,
                db.func.date(Question.created_at) == today
            ).count()

            if users_questions_today >= 3:
                flash("You have reached the daily limit for creating questions.")
                return redirect(url_for("dashboard"))

            new_question = Question(text_a=text_a, text_b=text_b, author=current_user, categories=categories)
            db.session.add(new_question)
            db.session.commit()
            flash("Question created successfully!")
            return redirect(url_for("dashboard"))
        return render_template("create_question.html")

    @app.route("/question/<int:question_id>")
    @login_required
    def view_question(question_id):
        question = Question.query.get_or_404(question_id)
        answers = Answer.query.filter_by(question=question).all()
        votes_a = sum(1 for answer in answers if answer.chosen_option == 'a')
        votes_b = sum(1 for answer in answers if answer.chosen_option == 'b')
        total_votes = len(answers)
        return render_template("view_question.html", question=question, votes_a=votes_a, votes_b=votes_b, total_votes=total_votes, user=current_user)

    @app.route("/question/<int:question_id>/edit", methods=["GET", "POST"])
    @login_required
    def edit_question(question_id):
        question = Question.query.get_or_404(question_id)
        if current_user.uid != question.author_id:
            flash("You can only edit your own questions.")
            return redirect(url_for("view_question", question_id=question.id))

        if request.method == "POST":
            question.text_a = request.form["text_a"]
            question.text_b = request.form["text_b"]
            categories_str = request.form.get("categories", "")
            
            categories = [cat.strip() for cat in categories_str.split(",") if cat.strip()]
            question.categories = categories
            
            db.session.commit()
            flash("Question updated successfully!")
            return redirect(url_for("view_question", question_id=question.id))

        return render_template("edit_question.html", question=question)

    @app.route("/vote/<int:question_id>", methods=["POST"])
    @login_required
    def vote(question_id):
        question = Question.query.get_or_404(question_id)
        chosen_option = request.form["chosen_option"]

        if chosen_option not in ['a', 'b']:
            flash("Invalid vote option.")
            return redirect(url_for("view_question", question_id=question.id))

        new_answer = Answer(question=question, user=current_user, chosen_option=chosen_option)
        db.session.add(new_answer)
        db.session.commit()
        flash("Your vote has been recorded!")
        return redirect(url_for("view_question", question_id=question.id))
        
    @app.route("/question/<int:question_id>/delete", methods=["POST"])
    @login_required
    def delete_question(question_id):
        question = Question.query.get_or_404(question_id)
        
        if current_user.uid != question.author_id:
            flash("You can only delete your own questions.")
            return redirect(url_for("view_question", question_id=question.id))
        
        Answer.query.filter_by(question=question).delete()
        
        db.session.delete(question)
        db.session.commit()
        
        flash("Question deleted successfully!")
        return redirect(url_for("dashboard"))
