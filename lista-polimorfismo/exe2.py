
class Ingresso:
    def __init__(self) -> None:
        self._valor = 600


class VIP(Ingresso):
    def __init__(self) -> None:
        super().__init__()
        self._adicional = 300


class Normal(Ingresso):

    def valorTotal(self):
        return self._valor
    
    def __str__(self):
        return f"Ingresso Normal foi adiquirido! Valor pago: {self._valor}"


class CamaroteInferior(VIP):
    def valorTotal(self):
        return self._valor + self._adicional
    
    def __str__(self):
        return f"Ingresso VIP foi adiquirido! Valor pago: {self._valor + self._adicional}"


class CamaroteSuperior(VIP):
    def __init__(self) -> None:
        super().__init__()
        self._adicionalCamarote = 100

    def valorTotal(self):
        return self._valor + self._adicional + self._adicionalCamarote
    
    def __str__(self):
        return f"Ingresso VIP foi adiquirido! Valor pago: {self._valor + self._adicional + self._adicionalCamarote}"


assento22 = Normal()

assento67 = CamaroteInferior()

assento02 = CamaroteSuperior()

print(assento22)

print(assento67)

print(assento02)
