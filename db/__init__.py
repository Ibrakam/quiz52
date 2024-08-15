# Импортируем что бы создать движок
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Указываем тип бд(sqlite, postgres)
SQLALCHEMY_DATABASE_URI = 'sqlite:///quiz.db'
# Создаем движок
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# Создаем сессию что бы хранить данные
SessionLocal = sessionmaker(bind=engine)
# Создаем полноченную базу
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
