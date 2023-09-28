"""
Sistema de Estoque e cliente fidelidade

"""


class User:
    def __int__(self, nome, cpf, senha):
        self._nome = nome
        self._cpf = cpf
        self._senha = senha

    # Cadastro do Usuário
    def cadastro(self):
        print("#################################################################")
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
    def addproduto(self, stock, produto):
        pass

    def removeproduto(self, stock, produto):
        pass

    # Manipular Produto
    def setNomeProduto(self, produto, nome):
        pass

    def setQuantidade(self, produto, value):
        pass

    def setValorProduto(self, produto, value):
        pass


class Stock:
    pass


class Product:
    def __int__(self):
        pass
