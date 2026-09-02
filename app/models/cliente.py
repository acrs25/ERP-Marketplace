from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Cliente(Base):
    __tablename__ = "clientes"

    # Identificador único do cliente (vendedor)
    id = Column(Integer, primary_key=True, index=True)

    # Nome do cliente (razão social ou nome fantasia)
    nome = Column(String, nullable=False)

    # CPF ou CNPJ do cliente
    # Usado para identificação fiscal e emissão de notas
    cpf_cnpj = Column(Integer, unique=True, nullable=False)

    # Email de contato do cliente
    email = Column(String, unique=True, nullable=False)

    # Endereço: CEP
    cep = Column(String, nullable=False)

    # Endereço: logradouro (rua, avenida, etc.)
    logradouro = Column(String, nullable=False)

    # Cidade
    cidade = Column(String, nullable=False)

    # Unidade federativa (estado)
    uf = Column(String, nullable=False)

    # Relacionamento ORM: um cliente pode ter vários produtos

    produtos = relationship("Produto", backref="cliente")

    # Relacionamento ORM: um cliente pode ter várias transações

    transacoes = relationship("Transacao", backref="cliente")
