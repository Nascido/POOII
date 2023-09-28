"""
Sistema de Estoque:

Progama de estoque de um Supermercado

"""


class User:
    def __init__(self, nome, senha):
        self._nome = nome
        self._senha = senha

    # Cadastro do Usuário
    def cadastro(self):
        print("\n\n#################################################################")
        print("---- Cadastro de Usuário ----")
        self._nome = input("Nome de Usuário: ")
        self._cpf = input("CPF: ")
        self._senha = input("Crie uma senha: ")

    # Getters
    def getname(self):
        return self._nome

    def getcpf(self):
        return self._cpf

    def getsenha(self):
        return self._senha

    def getuserinfo(self):
        return [self._nome, self._cpf, self._senha]

    # Setters
    def setnome(self, nome):
        self._nome = nome

    def setsenha(self, senha):
        self._senha = senha

    def setcpf(self, cpf):
        self._cpf = cpf

    def setuserinfo(self, info):
        self._nome, self._cpf, self._senha = info


class Cliente(User):
    def __init__(self, nome='', cpf=0, senha='cliente123'):
        super().__init__(nome, senha)
        # Itens reservados do cliente
        self._cpf = cpf
        self._itens = []

    def reservarProduto(self, produto):
        self._itens.append(produto)


class Staff(User):
    def __init__(self, nome='', senha='staff123'):
        super().__init__(nome, senha)

    # Manipular Estoque
    def adicionaProduto(self, stock, produto):
        pass

    def removeProduto(self, stock, produto):
        pass

    # Manipular Produto
    def setNomeProduto(self, produto, nome):
        pass

    def setQuantidade(self, produto, value):
        pass

    def setValorProduto(self, produto, value):
        pass


class Estoque:
    def __init__(self, produtos=None, clientes=None, funcionarios=None):

        # Produtos e usuários
        self._clients = clientes
        self._staff = funcionarios
        self._products = produtos

        # Setores dos produtos
        self._mercearia = []   # Setor 0
        self._frios = []       # Setor 1
        self._laticinios = []  # Setor 2
        self._bebidas = []     # Setor 3

        # Reservas dos Clientes
        self._reservas = []

    # Adicionar Usuários
    def addcliente(self, cliente):
        if self._clients is None:
            self._clients = []

        self._clients.append(cliente)

    def addstaff(self, funcionario):
        if self._staff is None:
            self._staff = []

        self._staff.append(funcionario)

    def addproduto(self, produto):
        if self._products is None:
            self._products = []

        self._products.append(produto)

    # Getters
    def getsetores(self):
        return self._mercearia, self._frios, self._laticinios, self._bebidas

    def getprodutos(self):
        return self._products

    def getclientes(self):
        return self._clients

    def getstaff(self):
        return self._staff

    def getreservas(self):
        return self._reservas


class Produto:
    def __init__(self, nome='', marca='', valor=0, setorDoProduto=0, quantidade=0):
        self._nome = nome
        self._marca = marca
        self._valor = valor
        self._setor = setorDoProduto
        self._quatidade = quantidade
        self._status = "disponivel"

    def registrarProduto(self):
        print("\n\n#################################################")
        print("----- Registro de Produto -----\n")
        self._nome = input("Nome do Produto: ")
        self._valor = int(input("Preço por unidade: "))
        self._setor = input("Qual o setor do produto: ")
        self._quantidade = input("Unidades no Estoque: ")
