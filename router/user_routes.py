from flask import render_template
from flask_login import current_user, login_required
from models import User, Question, Answer

def register_user_routes(app, db):
    @app.route("/user/<int:user_id>")
    @login_required
    def user_profile(user_id):
        user = User.query.get_or_404(user_id)
        questions = Question.query.filter_by(author=user).order_by(Question.created_at.desc()).all()
        
        answers = Answer.query.filter_by(user=user).order_by(Answer.created_at.desc()).all()
        
        answered_questions = []
        for answer in answers:
            question = answer.question
            answered_questions.append({
                'question': question,
                'chosen_option': answer.chosen_option,
                'created_at': answer.created_at
            })
            
        return render_template(
            "user_profile.html", 
            profile_user=user, 
            questions=questions, 
            answered_questions=answered_questions,
            user=current_user
        )
