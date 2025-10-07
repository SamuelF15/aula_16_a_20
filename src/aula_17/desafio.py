from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql.expression import func

engine = create_engine("sqlite:///desafio_aula_17.db", echo=True)

Base = declarative_base()

class Fornecedor(Base):
    __tablename__  = "fornecedores"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)
    endereco = Column(String(100), nullable=False)

class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(200))
    preco = Column(Integer)
    id_fornecedores = Column(Integer, ForeignKey('fornecedores.id'))

    fornecedor = relationship("Fornecedor")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


# try:
#     with Session() as session:
#         fornecedores = [
#             Fornecedor(id = 1, nome='Ana', telefone = 999517341, email = "ana.lobo@gmail.com", endereco = "Coronel Fabriciano, JK, Luiz gonzaga da silva, 193"),
#             Fornecedor(id = 2, nome='Beatriz', telefone = 31999517341, email = "beatriz.lobo@gmail.com", endereco = "Ipatinga, JK, Luiz gonzaga da silva, 193"),
#             Fornecedor(id = 3, nome='Souza', telefone = 999517341, email = "souza.lobo@gmail.com", endereco = "Timoteo, JK, Luiz gonzaga da silva, 193"),
#             Fornecedor(id = 4, nome='Samuel', telefone = 999971506, email = "samuel.lobo@gmail.com", endereco = "Vila Velha, JK, Luiz gonzaga da silva, 193"),
#             Fornecedor(id = 5, nome='Figueiredo', telefone = 9931127128, email = "figureido.lobo@gmail.com", endereco = "São sebatião do anta, JK, Luiz gonzaga da silva, 193")
#         ]
        


#         session.add_all(fornecedores)
#         session.commit()

# except SQLAlchemyError as e: 
#     print(f"Erro ao inserir fornecedores: {e}")
    
        
    
# try:
#     with Session() as session:
#         produtos = [
            
#             Produto(id = 1, nome = "produto 1", descricao = "Teste para o produto 1", preco = 123, id_fornecedores = 1),
#             Produto(id = 2, nome = "produto 2", descricao = "Teste para o produto 2", preco = 234, id_fornecedores = 2),
#             Produto(id = 3, nome = "produto 3", descricao = "Teste para o produto 3", preco = 345, id_fornecedores = 3),
#             Produto(id = 4, nome = "produto 4", descricao = "Teste para o produto 4", preco = 456, id_fornecedores = 4),
#             Produto(id = 5, nome = "produto 5", descricao = "Teste para o produto 5", preco = 567, id_fornecedores = 5)
#         ]
        
#         session.add_all(produtos)
#         session.commit()

# except SQLAlchemyError as e: 
#     print(f"Erro ao inserir fornecedores: {e}")
    

session = Session()

resultado = session.query(
    Fornecedor.nome,
    func.sum(Produto.preco).label('total_preco')
).join(Produto, Fornecedor.id == Produto.id_fornecedores
).group_by(Fornecedor.nome).all()

for nome, total_preco in resultado:
    print(f"Fornecedor: {nome}, Total Preço: {total_preco}")