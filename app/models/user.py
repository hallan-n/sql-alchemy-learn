from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    nome = Column(String(40))
    idade = Column(Integer)

    def __str__(self):
        return f"Id: {self.id}, Nome: {self.nome}, Idade: {self.idade}"
