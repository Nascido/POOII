
"""
Manual de Inicialização:

    1 - Rode este aqrquivo (sistemaP1) no mesmo diretório dos outros arquivos, sendo os
    ".txt" os bancos iniciais de dados e o arquivo supermercado.py sendo o retentor das classes.


    2 - Após a inicialização, você poderá escolher 3 opções para acessar o sistema:
    Caso queira testar todas as opções

       * LOGIN Cliente Já Registrado => CPF: 123  senha: 123

       * LOGIN Staff Já registrado => CPF: 321   senha: 321

       * CADASTRO => Apenas Seguir as opções apresentadas


    3 - Após entrar verá qual usuário está cadastrado no começo da tela e uma lista de
    produtos com seus nomes, marcas, valores, e quantidades no estoque apresentadas em uma linha.


    4 - Dependendo do login efetuado, aparecerá se você quer interagir com os produtos listados.
    Siga as instruções mostradas no console e verifique todas as mensagens printadas.


    5 - Tudo para rodar e interagir com o sistema está contido neste Folder.

"""

from supermercado import Cliente, Staff, Produto, Interface

# Leitura do Banco de Dados dos produtos
produtos = []
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        nome, marca, valor, setor, estoque = linha.strip().split('/')
        item = Produto(nome, marca, float(valor), int(setor), int(estoque))
        produtos.append(item)

# Leitura do Banco de Dados dos clientes
clientes = []
with open('clientes.txt', 'r') as arquivo:
    for linha in arquivo:
        nome, cpf, senha = linha.strip().split('/')
        cliente = Cliente(nome, int(cpf), senha)
        clientes.append(cliente)

# Leitura do Banco de dados dos funcionários
funcionarios = []
with open('funcionarios.txt', 'r') as arquivo:
    for linha in arquivo:
        nome, cpf, senha = linha.strip().split('/')
        funcionario = Staff(nome, int(cpf), senha)
        funcionarios.append(funcionario)

sistema = Interface(produtos, clientes, funcionarios)
sistema.iniciar()
