from app.database import SessionLocal
from app.models import Usuario, Cliente, Produto, Transacao
from datetime import datetime

db = SessionLocal()

# Usuário interno (funcionário da plataforma)
usuario = Usuario(
    id = "U001",
    nome="Maria Silva", 
    email="maria@erp.com", 
    senha_hash="hash123", 
    role="admin"
    )

# Cliente (vendedor)
cliente = Cliente(
    nome="Loja Exemplo", 
    cpf_cnpj="12345678901", 
    email="loja@exemplo.com", 
    cep="11775000",
    logradouro="Rua A, 123",
    cidade="Peruíbe",
    uf="SP"
    )

#Produto vinculado ao cliente

produto = Produto(
    nome="Camiseta Básica",
    sku="CAM123",
    preco_venda=50.00,
    taxa_comissao=0.10,
    estoque_atual=100,
    cliente=cliente
)

# Transação vinculada ao produto e cliente
transacao= Transacao(
    produto=produto,
    data_venda = int(datetime.now().timestamp()),
    quantidade=2,
    preco_venda_aplicado=50.00,
    taxa_comissao_aplicada=5.00,
    valor_liquido=95.00,
    cliente=cliente
    
)

# Inserir todos os registros
db.add_all([usuario, cliente, produto, transacao])
db.commit()
db.close()



