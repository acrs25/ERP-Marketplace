from sqlalchemy import Column, Integer, String
from app.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    # Identificador único do usuário (funcionário da plataforma)
    id = Column(String, primary_key=True, index=True)

    # Nome do usuário (ex: "Maria Silva")
    nome = Column(String, nullable=False)

    # Email do usuário: usado para login e comunicação interna
    email = Column(String, unique=True, nullable=False)

    # Senha armazenada como hash (nunca em texto puro)
    # Isso garante segurança na autenticação

    senha_hash = Column(String, nullable=True)

    # Cargo ou papel do usuário dentro da plataforma
    # Exemplo: "admin", "financeiro", "suporte"
    role = Column(String, nullable=False)
