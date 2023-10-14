from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_session():
    # Substitua 'seu_usuario', 'sua_senha', 'seu_host' e 'seu_banco_de_dados' pelos valores apropriados
    url = 'mysql+mysqlconnector://root:123456@localhost/sql_alchemy'
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    return Session()
