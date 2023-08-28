
"""
Trabalho 01 :  POO II

"""
import datetime


class Veiculo:
    def __int__(self, modelo, placa, documento, classe="normal"):
        self._modelo = modelo
        self._placa = placa
        self._documento = documento
        self._classe = classe
        self._alugado = False
        self._diaria = 50

    
class Carro(Veiculo):
    def __init__(self, assentos=5) -> None:
        super().__init__()
        self._assentos = assentos


class Moto(Veiculo):
    def __init__(self, cilindrada=150) -> None:
        super().__init__()
        self._cilindrada = cilindrada


class Cliente:
    def __init__(self, nome, idade, cpf, vencimentoCNH) -> None:
        self._nome = nome
        self._idade = idade
        self._cpf = cpf
        self._vencimentoCNH = vencimentoCNH

    def testarIdade(self):
        if self._idade < 24:
            print("O locatário deve ter idade superior a 24 anos!")
            del self


fulano = Cliente("Rafael", 34, 1111111, 5)
