import json
from flask_login import UserMixin
from sqlalchemy import Text, TypeDecorator
from sqlalchemy.ext.mutable import MutableList
from app import db
from datetime import datetime

class JSONEncodedList(TypeDecorator):
    impl = Text

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value

class User(db.Model, UserMixin):
    __tablename__ = "users"

    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    questions = db.relationship('Question', backref='author', lazy='dynamic')
    answers = db.relationship('Answer', backref='user', lazy='dynamic')

    def __repr__(self):
        return f"<User: {self.username}>"

    @property
    def id(self):
        return self.uid

class Question(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    text_a = db.Column(db.Text, nullable=False)
    text_b = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.uid'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    answers = db.relationship('Answer', backref='question', lazy='dynamic')
    categories = db.Column(MutableList.as_mutable(JSONEncodedList), default=list)

    def __repr__(self):
        return f"<Question: {self.text_a} or {self.text_b}>"

class Answer(db.Model):
    __tablename__ = "answers"

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.uid'), nullable=False)
    chosen_option = db.Column(db.Text, nullable=False) # 'a' or 'b'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Answer: User {self.user_id} voted on Question {self.question_id}>"
