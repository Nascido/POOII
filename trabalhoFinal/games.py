
from decks import Deck


class Player:
    def __init__(self, nome):
        self._name = nome
        self._hand = []
        self._wallet = 0

    def comprarCarta(self, deck):
        carta = deck.retirarCarta()
        self._hand.append(carta)

    def jogarCarta(self, indexCarta):
        return self._hand.pop(indexCarta)
    
    def getname(self):
        return self._name

    def __str__(self):
        return f"{self._name}: {self._hand}"
    

class Game:
    def __init__(self) -> None:
        self._game = None
        self._players = None

    def getplayers(self):
        return self._players

    def __str__(self):
        pass


class Blackjack(Game):
    pass
