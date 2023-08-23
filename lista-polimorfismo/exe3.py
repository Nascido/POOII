
class Imovel:
    def __init__(self, endereco, valor) -> None:
        self._endereco = endereco
        self._valor = valor


class Novo(Imovel):
    def __init__(self, endereco, valor) -> None:
        super().__init__(endereco, valor)

        self._adicional = 50000

    def __str__(self) -> str:
        return f"Imovel Novo com localização: {self._endereco}. Valor = {self._valor + self._adicional}"
    

class Velho(Imovel):
    def __init__(self, endereco, valor) -> None:
        super().__init__(endereco, valor)

        self._desconto = 0.75

    def __str__(self) -> str:
        return f"Imovel Novo com localização: {self._endereco}. Valor = {self._valor*self._desconto}"

"""
beiramar = Novo("Avenida beira mar", 155000)

mauro = Velho("Mauro Ramos", 100000)

print(beiramar)

print(mauro)
"""
