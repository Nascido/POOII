
"""
Trabalho 01 :  POO II

"""


class Veiculo:
    def __int__(self, modelo, placa, documento, classe="normal"):
        self._modelo = modelo
        self._placa = placa
        self._documento = documento
        self._classe = classe
        self._alugado = False
        self._diaria = 50

    
class Carro(Veiculo):
    def __init__(self, assentos = 5) -> None:
        super().__init__()
        self._assentos = assentos


class Moto(Veiculo):
    def __init__(self, cilindrada = 150) -> None:
        super().__init__()
        self._cilindrada = cilindrada


class PessoaFisica:
    def __int__(self, nome, idade, cpf, cnh):
        self._nome = nome
        self._idade = idade
        self._cpf = cpf
        self._cnh = cnh


class Locatario:
    def __init__(self, dias):
        self._dias = dias


class Cliente(PessoaFisica, Locatario):
  pass
