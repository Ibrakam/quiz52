from db import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime


# Таблица пользователей
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    level = Column(String, default="Select your level", nullable=False)
    datetime = Column(DateTime, default=datetime.now())


# Таблица вопросов
class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, autoincrement=True, primary_key=True)
    main_question = Column(String, nullable=False)
    v1 = Column(String)
    v2 = Column(String)
    v3 = Column(String)
    v4 = Column(String)
    correct_answer = Column(String, nullable=False)
    timer = Column(DateTime)


# Таблица для лидеров
class Result(Base):
    __tablename__ = "results"
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    correct_answer = Column(Integer, default=0)
    level = Column(String, nullable=False)

    user_fk = relationship(User, foreign_keys=[user_id], lazy='subquery')


# Ответы пользователя на вопрос
class UserAnswers(Base):
    __tablename__ = "user_answers"

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    question_id = Column(Integer, ForeignKey('questions.id'))
    level = Column(String, ForeignKey('users.level'))
    user_answer = Column(String)
    correctness = Column(Boolean, default=False)
    timer = Column(DateTime)

    user_fk = relationship(User, foreign_keys=[user_id], lazy='subquery')
    question_fk = relationship(Question, foreign_keys=[question_id], lazy='subquery')
