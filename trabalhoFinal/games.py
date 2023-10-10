from decks import Card


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

    def append(self, item):
        if type(item) is Card:
            self._hand.append(item)

        else:
            raise TypeError("the item type need to be Card")

    def remove(self, item):
        self._hand.remove(item)

    def insert(self, index, item):
        self._hand.insert(index, item)

    def getname(self):
        return self._name

    # Builtins
    def __getitem__(self, item):
        return self._hand[item]

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
        return f"{self._name}"


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
