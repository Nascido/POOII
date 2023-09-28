"""
Sistema de Estoque:

Progama de estoque de um Supermercado

"""


class User:
    def __init__(self, nome, cpf, senha):
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


class Cliente(User):
    def __init__(self, nome='', cpf=00000000000, senha='cliente123'):
        super().__init__(nome, cpf, senha)
        # Itens reservados do cliente
        self._itens = []

    def reservarProduto(self, produto):
        self._itens.append(produto)

    def __str__(self):
        return f"Cliente: {self._nome}"


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

    def __str__(self):
        return f"Funcionário {self._nome}"


class Estoque:
    def __init__(self, produtos=None, clientes=None, funcionarios=None):

        # Produtos e usuários
        self._clients = clientes
        self._staff = funcionarios
        self._produtos = produtos

        # Setores dos produtos
        self._mercearia = []   # Setor 0
        self._frios = []       # Setor 1
        self._laticinios = []  # Setor 2
        self._bebidas = []     # Setor 3

        self.organizarSetores()

        # Reservas dos Clientes
        self._reservas = []

    # Organizar Estoque
    def organizarSetores(self):
        for produto in self._produtos:
            setor = produto.getsetor()
            match setor:
                case 0:
                    self._mercearia.append(produto)
                case 1:
                    self._frios.append(produto)
                case 2:
                    self._laticinios.append(produto)
                case 3:
                    self._bebidas.append(produto)
                case _:
                    print(f"Setor Inexistente para {produto.getnome()}")

    # Adicionar Usuários
    def addcliente(self, cliente):
        if self._clients is None:
            self._clients = []

        self._clients.append(cliente)

    def addproduto(self, produto):
        if self._produtos is None:
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
        # Informações do produto
        self._nome = nome
        self._marca = marca
        self._valor = valor
        self._setor = setorDoProduto
        self._quantidade = quantidade

        self._status = "disponivel"

        self.disponibilidade()

    def registrarProduto(self):
        print("\n\n#################################################")
        print("----- Registro de Produto -----\n")
        self._nome = input("Nome do Produto: ")
        self._valor = int(input("Preço por unidade: "))
        self._setor = input("Qual o setor do produto: ")
        self._quantidade = input("Unidades no Estoque: ")

    def disponibilidade(self):
        if self._quantidade <= 0:
            self._status = 'indisponível'
            return False

        else:
            self._status = 'disponivel'
            return True

    # Getters
    def getsetor(self):
        return self._setor

    def getnome(self):
        return self._nome

    def getmarca(self):
        return self._marca

    def getvalor(self):
        return self._valor

    def getquantidade(self):
        return self._quantidade

    def getstatus(self):
        self.disponibilidade()
        return self._status

    def __str__(self):
        return f"{self._nome}({self._marca}): R$ {self._valor} [ESTOQUE: {self._quantidade}]"


class Interface:
    def __init__(self, produtos=None, clientes=None, funcionarios=None):
        # Atributos ativos e em uso
        self.estoque = Estoque(produtos, clientes, funcionarios)
        self.usuario = None

        self._clientes = self.estoque.getclientes()
        self._staff = self.estoque.getstaff()

    def iniciar(self):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
        print("Bem vindo ao mercado SUPERDINO!")
        print("Escolha a opção desejada:")

        print("1 - Login Cliente")
        print("2 - Cadastro Cliente")
        print("3 - Acesso para pessoal autorizado\n\n")

        op = int(input("Opção: "))

        match op:
            case 1:
                self.telaLogin('CLIENTE')
            case 2:
                self.telaCadastro()
            case _:
                self.telaLogin('FUNCIONÁRIO')

    def telaLogin(self, usuario):
        if usuario == 'CLIENTE':
            usuariosPermitidos = self._clientes

        else:
            usuariosPermitidos = self._staff

        op = 0
        while op == 0:
            print("\n\n######################################")
            print(f"LOGIN DE {usuario}\n")
            cpf = int(input("CPF: "))
            senha = input("Senha: ")
            for user in usuariosPermitidos:
                cpfRegistrado = user.getcpf()
                if cpf == cpfRegistrado:
                    senhaRegistrada = user.getsenha()
                    if senha == senhaRegistrada:
                        self.usuario = user
                        self.produtosEstoque()
                        return 0

            print("\n\n\nCPF OU SENHA INCORRETA!!")
            print("1 - Voltar ao Início")
            print("0 - Refazer Login")
            op = int(input("Opção: "))

        self.iniciar()
        return 0

    def telaCadastro(self):
        print("\n\n########################################")
        print("CADASTRO DE CLIENTE")
        usuariosCadastrados = self._clientes
        nome = input("Nome: ")
        cpf = int(input("CPF: "))
        for user in usuariosCadastrados:
            cpfcadastrado = user.getcpf()
            if cpf == cpfcadastrado:
                print("\n\nCPF JÁ CADSTRADO!!")
                print("1 - Voltar ao Início")
                print("0 - Refazer Cadastro")
                op = int(input("Opção: "))
                if op == 0:
                    self.telaCadastro()
                    return 0
                else:
                    self.iniciar()
                    return 0

        senha = input("Senha: ")

        self.usuario = Cliente(nome, cpf, senha)
        self.estoque.addcliente(self.usuario)

        self.produtosEstoque()

    def produtosEstoque(self):
        setores = self.estoque.getsetores()
        print("\n\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("PRODUTOS EM ESTOQUE:\n")
        i = 1
        j = 0
        produtosDisponiveis = []
        produtosIndisponiveis = []
        nomes = ["MERCEARIA", "FRIOS", "LATICÍNIOS", "BEBIDAS"]
        for setor in setores:
            print(f"\n{nomes[j]}")
            j += 1
            for produto in setor:
                if produto.disponibilidade():
                    produtosDisponiveis.append(produto)
                    print(f"{i} - {produto}")
                    i += 1

                else:
                    produtosIndisponiveis.append(produto)
