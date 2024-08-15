from db import get_db
from db.models import User, UserAnswers, Question, Result


def get_all_users():
    with next(get_db()) as db:
        all_users = db.query(User).all()
        return all_users


# Регистрация пользователя
def register_user_db(name, phone_number, level):
    with next(get_db()) as db:
        checker = db.query(User).filter_by(phone_number=phone_number).first()
        if checker:
            return checker
        new_user = User(name=name, phone_number=phone_number, level=level)
        db.add(new_user)
        db.commit()
        return "Успешно зарегестрировались"


# Ответы пользователя
def user_answer_db(q_id, user_answer, user_id, level):
    with next(get_db()) as db:
        exact_question = db.query(Question).filter_by(id=q_id).first()
        if exact_question:
            if exact_question.correct_answer == user_answer:
                correctness = True
            else:
                correctness = False
            new_answer = UserAnswers(user_id=user_id, q_id=q_id, level=level, correctness=correctness)
            db.add(new_answer)
            db.commit()
            if correctness:
                user_result = db.query(Result).filter_by(user_id=user_id).first()
                if user_result:
                    user_result.correct_answer += user_answer
                    db.commit()
                    return "Плюс один бал"
            else:
                print("Не сработало")
                return False
        else:
            return "Такого вопроса нету"


def get_result_user_db(user_id):
    with next(get_db()) as db:
        user_result = db.query(Result).filter_by(user_id=user_id).first()
        return user_result
