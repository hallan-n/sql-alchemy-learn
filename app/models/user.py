from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import re

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40))
    idade = Column(Integer)




for a in vars(User):
    if not a.startswith("_"):
        print(a)