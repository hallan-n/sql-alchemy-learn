from app.database.connection import get_session
from app.models.user import User
from app.models.base_model import BaseModel, Base
from dotenv import load_dotenv

load_dotenv()

session = get_session()

Base.metadata.create_all(session.bind)


def create(value: BaseModel):
    if value.__tablename__ == "user":
        if value.id:
            print("Não é permitido passar ID ao criar usuário")
            return
        print(f"Criado com sucesso. Dados: {value}")
        session.add(value)
        session.commit()
    session.close()


def get_all(model):
    if model == "user":
        users = session.query(User).all()
        session.close()
        return users


def get_for_id(id, model):
    if model == "user":
        user = session.query(User).filter(User.id == id).first()
        session.close()
        return user


def update(value: BaseModel):
    if _verify_fields(value):
        print(f"Atualizou com os dados: {value}")
        session.merge(value)
        session.commit()
    else:
        print("O objeto Pessoa não possui um ID definido.")
    session.close()


def delete(idx, model):
    if model == "user":
        user = _verify_fields(User(id=idx))
        if user[0]:
            print(f"Deletado os dados os dados: {user[1]}")
            session.delete(user[1])
            session.commit()
    else:
        print("O objeto Pessoa não possui um ID definido.")
    session.close()


def _verify_fields(value: BaseModel):
    if value.__tablename__ == "user":
        user_find = session.query(User).filter(User.id == value.id).first()
        if user_find:
            return True, user_find
        else:
            return False
