from sqlalchemy import Column, Integer, String
from app.models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    nome = Column(String(40))
    idade = Column(Integer)

    def __str__(self):
        return f"Id: {self.id}, Nome: {self.nome}, Idade: {self.idade}"
