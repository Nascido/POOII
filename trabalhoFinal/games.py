from decks import Card


class Player:
    def __init__(self, nome, fichas):
        self._name = nome
        self._hand = []
        self._fichas = fichas
        self.index = 0

    def comprarCarta(self, deck):
        carta = deck.pop()
        self._hand.append(carta)

    def apostar(self, valor):
        if self._fichas >= valor:
            self._fichas -= valor
            return valor
        else:
            print("Valor maior que o número de fihcas")
            return 0

    def receber(self, valor):
        self._fichas += valor

    def sum(self):
        soma = 0
        for carta in self._hand:
            soma += int(carta)

        return soma

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

    def __int__(self):
        return self._fichas

    def __str__(self):
        return f"{self._name}"


class Game:
    def __init__(self, players, caixa) -> None:
        self._players = players
        self._pote = 0
        self._caixa = caixa

    def getplayers(self):
        return self._players


class Blackjack(Game):
    def __init__(self, players, caixa, apostaInicial=20) -> None:
        super().__init__(players, caixa)
        self._dealerHand = []
        self._rodadas = 0
        self._apostaInicial = apostaInicial

    def iniciar(self):
        participantes = []
        for player in self._players:
            participar = bool(input(f"{player} vai participar?"))

            if participar:
                participantes.append(player)

    def rodada(self, players):
        pass
