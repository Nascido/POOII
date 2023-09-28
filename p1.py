"""
Sistema de Estoque:

Progama de estoque de um Supermercado

"""


class User:
    def __int__(self, nome, cpf, senha):
        self._nome = nome
        self._cpf = cpf
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


class Client(User):
    def __int__(self, nome='', cpf=0, senha='cliente123'):
        super().__int__(nome, cpf, senha)
        # Itens reservados do cliente
        self._itens = []

    def reservarProduto(self, produto):
        self._itens.append(produto)


class Staff(User):
    def __init__(self, nome='', cpf=0, senha='staff123'):
        super().__init__(nome, cpf, senha)

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


class Stock:
    def __init__(self, produtos=None, clientes=None, funcionarios=None, unidade='centro'):
        # Localidade do Estoque
        self._unidade = unidade

        # Produtos e usuários
        self._clients = clientes
        self._staff = funcionarios
        self._products = produtos

        # Setores dos produtos

        self._mercearia = []   # Setor 1
        self._frios = []       # Setor 2
        self._laticinios = []  # Setor 3
        self._bebidas = []     # Setor 4
        self._higiene = []     # Setor 5

        # Reservas dos Clientes
        self._reservados = []

        self._data = [self._products, self._staff, self._clients]

        for resgistro in self._data:
            if resgistro is None:
                resgistro = []

    def addclient(self, cliente):
        self._clients.append(cliente)

    def addstaff(self, funcionario):
        self._staff.append(funcionario)


class Product:
    def __int__(self, nome='', valor=0, setorDoProduto=0):
        self._nome = nome
        self._valor = valor
        self._setor = setorDoProduto

        self._barcode = 0

    def registrarProduto(self):
        print("\n\n#################################################")
        print("----- Registro de Produto -----\n")
        self._nome = input("Nome do Produto: ")
        self._valor = int(input("Preço por unidade: "))
        self._setor = input("Qual o setor do produto: ")
