from app.database.connection import get_session
from app.models.user import User
from app.models.base_model import BaseModel, Base
from dotenv import load_dotenv
from copy import copy

load_dotenv()

session = get_session()

Base.metadata.create_all(session.bind)


def get_all_users():
    user = session.query(User).all()
    session.close()
    return user


def get_user_for_id(id):
    users = session.query(User).filter(User.id == id)
    session.close()
    return users


def update(user: BaseModel):
    if _verify_fields(user):
        session.merge(user)
        session.commit()
    session.close()
    


def _verify_fields(value: User):
    if value.__tablename__ == "user":
        user_find = session.query(User).filter(User.id == value.id).first()
        if user_find:
            print(f"Atualizou com os dados: {value}")
            return True
        else:
            print("O objeto Pessoa não possui um ID definido.")
            return False
       
