
"""
Trabalho 01 :  POO II

"""
import datetime


class Veiculo:
    def __int__(self):
        self._modelo = None
        self._placa = None
        self._documento = None
        self._classe = None
        self._cor = None
        self._alugado = False
        self._diaria = 50

        self.registrarVeiculo()

    def registrarVeiculo(self):
        print("Por favor insira as informações para o registro do Veículo")
        self._modelo = input("Modelo do Veículo: ")
        self._placa = input("Placa: ")
        self._documento = input("Documentação: ")
        self._classe = input("Normal ou de luxo? ")

    def setDados(self, data):
        self._modelo = data[0]
        self._placa = data[1]
        self._documento = data[2]
        self._classe = data[3]

    
class Carro(Veiculo):
    def __init__(self, assentos=5, arcondicionado=True) -> None:
        super().__init__()
        self._assentos = assentos
        self._arcondicionado = arcondicionado


class Moto(Veiculo):
    def __init__(self, cilindrada=150) -> None:
        super().__init__()
        self._cilindrada = cilindrada


class Cliente:
    def __init__(self, nome=None, idade=None, cpf=None, vencimentoCNH="26/01/2001") -> None:
        self._nome = nome
        self._idade = idade
        self._cpf = cpf
        self._vencimentoCNH = datetime.datetime.strptime(vencimentoCNH, "%d/%m/%y")
        self._permitido = False

    def registrarCliente(self):
        print("Por favor insira os dados do cliente locatário")
        self._nome = input("Nome: ")
        self._idade = input("Idade: ")
        self._cpf = input("CPF: ")
        self._vencimentoCNH = input("Vencimento da CNH (dd/mm/yy): ")
        self.testarIdade()
        self.testarValidade()

    def setDados(self, data):
        self._nome = data[0]
        self._idade = data[1]
        self._cpf = data[2]
        self._vencimentoCNH = data[3]

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
        else:
            self._permitido = True


cliente_rafael = Cliente("Rafael", 22, 12471455905, "10/06/24")
cliente_pedro = Cliente("Pedro", 25, 11112222333, "20/08/27")
cliente_tobias = Cliente("Tobias", 34, 22222233333, "03/03/25")

cliente_sem_nome = Cliente()
