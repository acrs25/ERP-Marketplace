from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from app.database import Base

# Cada classe aqui representa uma tabela no banco de dados.
# O SQLAlchemy transforma essa classe em SQL real quando rodamos as migrações.


class Produto(Base):
    __tablename__ = "produtos"  # nome da tabela no banco

    # Abaixo definimos as colunas da tabela:
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)  # nome do produto

    # SKU é um código único para identificar o produto.
    # unique=True garante que não haverá dois produtos com o mesmo SKU.

    sku = Column(String, unique=True, nullable=False)

    # preço de venda: quanto o produto será vendido ao cliente.
    preco_venda = Column(Float, nullable=False)

    # taxa de comissão da plataforma (% sobre a venda)
    taxa_comissao = Column(Float, nullable=False)

    # Estoque atual: quantidade disponível para venda no marketplace
    estoque_atual = Column(Integer, default=0)
    
    #Chave estrangeira cliente
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    cliente = relationship("Cliente", back_populates="produtos")
    transacoes = relationship("Transacao", back_populates="produto")
