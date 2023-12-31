
"""
Trabalho 01 :  POO II

    Implementação de um sistema de Aluguel de Veiculos

"""
import datetime


class Veiculo:
    def __int__(self):
        self._modelo = None
        self._placa = None
        self._cor = None
        self._cliente = None
        self._tipo = ''
        self._dataDevolucao = None
        self._dataAluguel = None

    def registrarVeiculo(self):
        print("###################################################################################")
        print("Por favor insira as informações para o registro do Veículo")
        self._modelo = input("Modelo do Veículo: ")
        self._cor = input("Cor: ")
        self._placa = input("Placa: ")

    def alugar(self, cliente, dias):
        if not self._alugado:
            if cliente.getpermissao():
                if cliente.havetipoCNH(self._tipo):
                    self._alugado = True
                    self._cliente = cliente
                    self._cliente.addVeiculo(self)
                    today = datetime.datetime.now()
                    self._dataDevolucao = today + datetime.timedelta(dias)
                    self._dataAluguel = today

                    return True
                else:
                    print(f"Cliente {cliente.getname()} não possui CNH para este veículo")

            else:
                print(f"Cliente {cliente.getname()} sem permissão para alugar!")

        else:
            print(f"Veículo {self._modelo} já está alugado!")

        return False

    def devolver(self):
        if self._alugado:
            self._alugado = False
            self._cliente.removeVeiculo(self)
            today = datetime.datetime.now()
            diff = (today - self._dataAluguel).days

            if diff == 0:
                valorFinal = self._diaria
            else:
                valorFinal = self._diaria*diff

            print(f"Devolução! Veículo {self._modelo} por {self._cliente.getname()}. Total a pagar = R$ {valorFinal}")

            return True
        else:
            print(f"Veiculo {self._modelo} não está alugado")
            return False

    def setdata(self, data):
        """
        data = [Modelo, cor, placa]
        """

        self._modelo = data[0]
        self._cor = data[1]
        self._placa = data[2]

    def _setalugado(self, estado):
        self._alugado = estado

    def _setdiaria(self, valor):
        self._diaria = valor

    def getalugado(self):
        return self._alugado

    def getdiaria(self):
        return self._diaria

    def getdiaDevolucao(self):
        return self._dataDevolucao

    def getdiaAlugada(self):
        return self._dataAluguel


class Carro(Veiculo):
    def __init__(self, assentos=5, arcondicionado=False, classe="normal") -> None:
        super().__init__()
        self._assentos = assentos
        self._arcondicionado = arcondicionado
        self._classe = classe
        self._tipo = 'B'
        self._diaria = 50
        self._alugado = False
        self.calculaDiaria()

    def calculaDiaria(self):
        if self._assentos > 5:
            self._diaria *= 1.5
        if self._arcondicionado:
            self._diaria += 20
        if self._classe == "luxo":
            self._diaria *= 1.5

    def __str__(self) -> str:
        if self._alugado:
            return f"Carro modelo {self._modelo} com placa {self._placa} alugado por {self._cliente.getname()}."
        else:
            return f"Carro modelo {self._modelo} com placa {self._placa} disponível para alugar."


class Moto(Veiculo):
    def __init__(self, cilindrada=150, classe="normal") -> None:
        super().__init__()
        self._cilindrada = cilindrada
        self._classe = classe
        self._tipo = 'A'
        self._diaria = 30
        self._alugado = False
        self.calculaDiaria()

    def calculaDiaria(self):
        if 150 <= self._cilindrada < 300:
            self._diaria += 2

        elif 300 <= self._cilindrada < 500:
            self._diaria += 10

        else:
            self._diaria += 20

        if self._classe == "luxo":
            self._diaria *= 1.5

    def __str__(self) -> str:
        if self._alugado:
            return f"Moto modelo {self._modelo} com placa {self._placa} alugada por {self._cliente.getname()}."
        else:
            return f"Moto modelo {self._modelo} com placa {self._placa} disponível para alugar."


class Cliente:
    def __init__(self, nome="desconhecido", idade=18, tipoCNH="", vencimentoCNH="01/01/01", registrar=False) -> None:
        self._nome = nome
        self._idade = idade
        self._tipoCNH = tipoCNH
        self._vencimentoCNH = datetime.datetime.strptime(vencimentoCNH, "%d/%m/%y")
        self._registrado = registrar
        self._permitido = False
        self._veiculosAlugados = []

        if self._registrado:
            self.testarPermissao()

    def registrarCliente(self):
        print("###################################################################################")
        print("Por favor insira os dados do cliente locatário")
        self._nome = input("Nome: ")
        self._idade = int(input("Idade: "))
        self._tipoCNH = input("Tipo CNH: ")
        vencimentoCNH = input("Vencimento da CNH (dd/mm/yy): ")
        self._vencimentoCNH = datetime.datetime.strptime(vencimentoCNH, "%d/%m/%y")
        self._registrado = True
        apto = self.testarPermissao()

        if apto:
            return True
        
        return False

    def testarValidade(self):
        today = datetime.datetime.now()
        diff = (self._vencimentoCNH - today).days
        if diff < 0:
            print(f"Locatário {self._nome} com CNH vencida!")
            return False
        
        return True

    def testarIdade(self):
        if self._idade < 20:
            print(f"O locatário {self._nome} deve ter idade superior a 22 anos!")
            return False
        
        return True

    def testarPermissao(self):
        if self.testarIdade() and self.testarValidade():
            self._permitido = True
            return True
        
        return False

    def addVeiculo(self, veiculo):
        self._veiculosAlugados.append(veiculo)

    def removeVeiculo(self, veiculo):
        self._veiculosAlugados.remove(veiculo)

    def havetipoCNH(self, tipo):
        if self._tipoCNH.find(tipo) != -1:
            return True
        
        return False

    def _setdata(self, data):
        """

        data = [nome, idade, tipoCNH, vencimentoCNH]

        """
        self._nome = data[0]
        self._idade = data[1]
        self._tipoCNH = data[2]
        vencimentoCNH = data[3]
        self._vencimentoCNH = datetime.datetime.strptime(vencimentoCNH, "%d/%m/%y")
        self.testarPermissao()

    def _setidade(self, idade):
        self._idade = idade
        self.testarIdade()

    def _settipoCNH(self, tipo):
        self._tipoCNH = tipo

    def _setCNH(self, cnh):
        vencimentoCNH = cnh
        self._vencimentoCNH = datetime.datetime.strptime(vencimentoCNH, "%d/%m/%y")
        self.testarValidade()

    def getname(self):
        return self._nome

    def getpermissao(self):
        return self._permitido

    def gettipoCNH(self):
        return self._tipoCNH

    def __str__(self) -> str:
        if self._permitido and self._registrado:
            if self.havetipoCNH('AB'):
                return f"Cliente {self._nome}: Permissão para Carro e Moto"
            elif self.havetipoCNH('A'):
                return f"Cliente {self._nome}: Permissão para Moto"
            elif self.havetipoCNH('B'):
                return f"Cliente {self._nome}: Permissão para Carro"
            else:
                return f"Cliente {self._nome}: Sem Permissão"
        else:
            return f"Cliente {self._nome}: Sem Permissão"
