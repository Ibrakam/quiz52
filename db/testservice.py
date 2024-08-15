from db import get_db
from db.models import Question, Result


def add_question_db(main_question, v1, v2, v3, v4, correct_answer):
    with next(get_db()) as db:
        new_question = Question(main_question=main_question, v1=v1, v2=v2, v3=v3, v4=v4, correct_answer=correct_answer)
        db.add(new_question)
        db.commit()
        return "Вопрос успешно добавлен"


# Получить первые 20 вопросов
def get_questions():
    with next(get_db()) as db:
        question = db.query(Question).all()
        return question[:20]


# Топ 10 лидеров
def get_10_leaders():
    with next(get_db()) as db:
        leaders = db.query(Result.user_id).order_by(Result.correct_answer.desc())
        return leaders[:10]
