

class Player:
    def __init__(self, nome):
        self._name = nome
        self._hand = []
        self._wallet = 0
        self.index = 0

    def comprarCarta(self, deck):
        carta = deck.pop()
        self._hand.append(carta)

    def pop(self, indexCarta=0):
        return self._hand.pop(indexCarta)
    
    def getname(self):
        return self._name

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self._hand):
            result = self._hand[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __len__(self):
        return len(self._hand)

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
