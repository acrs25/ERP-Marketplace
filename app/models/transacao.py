from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Transacao(Base):
    __tablename__ = "transacoes"

    # Identificador único da transação
    id = Column(Integer, primary_key=True, index=True)

    # produto_id: chave estrangeira que aponta para a tabela Produto
    # Isso garante que cada transação esteja vinculada a um produto existente

    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)

    # Relacionamento ORM: permite acessar os dados do produto diretamente
    produto = relationship("Produto")

    # Data da venda: quando a transação ocorreu
    data_venda = Column(Integer, nullable=False)

    # Quantidade vendida do produto nesta transação
    quantidade = Column(Integer, nullable=False)

    # Preço de venda aplicado na época da transação
    # Pode ser diferente do preco_venda atual do Produto

    preco_venda_aplicado = Column(Float, nullable=False)

    # Taxa de comissão aplicada na época da venda

    taxa_comissao_aplicada = Column(Float, nullable=False)

    # Valor líquido repassado ao vendedor
    # Calculado como (preco_venda_aplicado * quantidade) - comissão

    valor_liquido = Column(Float, nullable=False)
