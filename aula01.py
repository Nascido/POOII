
class Interruptor:
    def __init__(self, comodo) -> None:
        self._comodo = comodo
        self._ligado = False
    
    def interact(self):
        if self._ligado:
            self._ligado = False
        else:
            self._ligado = True

    def status (self):
        return self._ligado

    def __str__(self) -> str:
        if self._ligado:
            return f"Interruptor: {self._comodo} is ON"
        else:
            return f"Interruptor: {self._comodo} is OFF"


class Lampada:
    def __init__(self, comodo) -> None:
        self._comodo = comodo
        self.__ligado = False
        self.__connected = ("disconnected", False)

    def connect(self, interruptor):
        self.interruptor = interruptor
        self.__connected = ("connected", True)

    def status(self):
        return self.__ligado

    def verify(self):
        if self.interruptor.status():
            self.__ligado = True
        else:
            self.__ligado = False

    def __str__(self) -> str:
        if self.__connected[1]:
            self.verify()
        if self.__ligado:
            return f"Lampada {self._comodo} is {self.__connected[0]} and ON"
        else:
            return f"Lampada {self._comodo} is {self.__connected[0]} and OFF"
        

#Criando lampada e Interruptor
lampadaSala = Lampada("sala")
interruptorSala = Interruptor("Sala")

print(lampadaSala)
print(interruptorSala)
print("")

#conectando Ambos
lampadaSala.connect(interruptorSala)
print(lampadaSala)

#interagindo com o Interruptor
interruptorSala.interact()
print(lampadaSala)

#interagindo de novo
interruptorSala.interact()
print(lampadaSala)

#interagindo de novo
interruptorSala.interact()
print(lampadaSala)