from models.user import User, Base
from database.connection import get_session
session = get_session()
Base.metadata.create_all(session.bind)
user1 = User(nome="Hállan", idade=22)
session.add(user1)
session.commit()
session.close()
