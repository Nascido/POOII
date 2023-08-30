
"""
Trabalho 01 :  POO II

"""
import datetime


class Veiculo:
    def __int__(self):
        self._modelo = None
        self._placa = None
        self._documento = None
        self._cor = None
        self._alugado = False
        self._diaria = 50

    def registrarVeiculo(self):
        print("###################################################################################")
        print("Por favor insira as informações para o registro do Veículo")
        self._modelo = input("Modelo do Veículo: ")
        self._placa = input("Placa: ")
        self._documento = input("Documentação: ")

    def setDados(self, data):
        self._modelo = data[0]
        self._placa = data[1]
        self._documento = data[2]

    def setAlugado(self, estado):
        self._alugado = estado

    def setDiaria(self, valor):
        self._diaria = valor

    def getAlugado(self):
        return self._alugado

    def getDiaria(self):
        return self._diaria


class Carro(Veiculo):
    def __init__(self, assentos=5, arcondicionado=True, classe="normal") -> None:
        super().__init__()
        self._assentos = assentos
        self._arcondicionado = arcondicionado
        self._classe = classe


class Moto(Veiculo):
    def __init__(self, cilindrada=150, classe="normal") -> None:
        super().__init__()
        self._cilindrada = cilindrada
        self._classe = classe

    
class Cliente:
    def __init__(self, nome=None, idade=None, cpf=None, vencimentoCNH="26/01/01") -> None:
        self._nome = nome
        self._idade = idade
        self._cpf = cpf
        self._vencimentoCNH = datetime.datetime.strptime(vencimentoCNH, "%d/%m/%y")
        self._permitido = False

    def registrarCliente(self):
        print("###################################################################################")
        print("Por favor insira os dados do cliente locatário")
        self._nome = input("Nome: ")
        self._idade = int(input("Idade: "))
        self._cpf = input("CPF: ")
        vencimentoCNH = input("Vencimento da CNH (dd/mm/yy): ")
        self._vencimentoCNH = datetime.datetime.strptime(vencimentoCNH, "%d/%m/%y")
        self.testarPermissao()

    def setDados(self, data):
        self._nome = data[0]
        self._idade = data[1]
        self._cpf = data[2]
        vencimentoCNH = data[3]
        self._vencimentoCNH = datetime.datetime.strptime(vencimentoCNH, "%d/%m/%y")

    def setIdade(self, idade):
        self._idade = idade

    def setCNH(self, cnh):
        vencimentoCNH = cnh
        self._vencimentoCNH = datetime.datetime.strptime(vencimentoCNH, "%d/%m/%y")

    def getName(self):
        return self._nome

    def testarValidade(self):
        today = datetime.datetime.now()
        diff = (self._vencimentoCNH - today).days
        if diff < 0:
            self._permitido = False
            print("Locatário com CNH vencida!")
        else:
            self._permitido = True

    def testarIdade(self):
        if self._idade < 22:
            print("O locatário deve ter idade superior a 22 anos!")
            self._permitido = False
        else:
            self._permitido = True

    def testarPermissao(self):
        self.testarValidade()
        self.testarIdade()


cliente_rafael = Cliente("Rafael", 22, 12471455905, "10/06/24")
cliente_pedro = Cliente("Pedro", 25, 11112222333, "20/08/27")
cliente_tobias = Cliente("Tobias", 34, 22222233333, "03/03/25")
