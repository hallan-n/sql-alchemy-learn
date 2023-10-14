from app.database.connection import get_session
from app.models.user import User, Base
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


def update(user: User):
    # user_find = session.query(User).filter(User.id == user.id).first()

    if not user.id:
        print("O objeto Pessoa não possui um ID definido.")
        return

    session.add(user)

    # Faça um commit para salvar as alterações no banco de dados
    session.commit()
    session.close()


def _verify_fields(value):
    if value == "user":
        user_vars = []
        for var in vars(User):
            if not var.startswith("_"):
                user_vars.append(var)
        return user_vars
