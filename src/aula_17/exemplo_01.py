from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String

engine = create_engine("sqlite:///meubanco_aula_17.db", echo=True)
# conn = create_engine("duckdb:///:duckdb_aula_17.db ", echo=True).connect()
print("Conexão criada com sucesso!")


Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)


Base.metadata.create_all(engine)
print("Tabela criada com sucesso!")

from sqlalchemy import delete

Session = sessionmaker(bind=engine)
session = Session()

stmt = delete(Usuario).where(Usuario.id == 2)
session.execute(stmt)
session.commit()
print("Registro deletado com sucesso!")
session.close()
###############################################################################
Session = sessionmaker(bind=engine)
session = Session()
print("Sessão criada com sucesso!")

novo_usuario = Usuario(nome="Beatriz", idade=31)
session.add(novo_usuario)
session.commit()
print("Usuário adicionado com sucesso!")

usuario = session.query(Usuario).filter_by(nome="Beatriz").first()
print(f"Usuário encontrado: {usuario.nome}, Idade: {usuario.idade}")
session.close()
###############################################################################

from sqlalchemy.orm import sessionmaker
# assumindo que engine já foi criado

Session = sessionmaker(bind=engine)
session = Session()

try:
    novo_usuario = Usuario(nome='Ana', idade=31)
    session.add(novo_usuario)
    session.commit()
except:
    session.rollback()
    raise
finally:
    session.close()

