from supermercado import Estoque, Cliente, Staff, Produto

produtos = []
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        nome, marca, valor, setor, estoque = linha.strip().split('/')
        item = Produto(nome, marca, float(valor), int(setor), int(estoque))
        produtos.append(item)

clientes = []
with open('clientes.txt', 'r') as arquivo:
    for linha in arquivo:
        nome, cpf, senha = linha.strip().split('/')
        cliente = Cliente(nome, int(cpf), senha)
        clientes.append(cliente)
