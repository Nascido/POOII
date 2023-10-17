from decks import Deck, Card


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

    def getfichas(self):
        return self._fichas

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
    def __init__(self, players) -> None:
        self._players = players
        self._pote = 0
        self._caixa = 0

    def getplayers(self):
        return self._players


class Poker(Game):
    def __init__(self, players, bigBlind=50, aumentoBlind=50) -> None:
        super().__init__(players)
        # Até 5 cartas
        self._tableCards = []

        # fase 0: Pre-flop
        # fase 1: Flop
        # fase 2: Turn
        # fase 3: River
        # fase 4: Showdown
        self._fase = 0

        self._rodadas = 0

        # Blinds
        self._small = bigBlind/2
        self._big = bigBlind
        self._passo = aumentoBlind

    def iniciar(self):
        participantes = []
        for player in self._players:
            fichas = player.getfichas()
            if fichas >= self._big:
                participantes.append(player)

        tam = len(participantes)

        while self._fase < 4 and tam > 1:
            baralho = Deck()
            baralho.shuffle()

            if self._fase == 0:
                small = participantes[0]
                big = participantes[1]

                small.apostar(self._small)
                big.apostar(self._big)

                baralho.distribuir(self._players, 2)

            elif self._fase == 1:
                baralho.distribuir([self._tableCards], 3)

            else:
                self._tableCards.append(baralho.pop())

    def rodadaDeApostas(self, participantes):
        pass

    def definirGanhador(self):
        pass

    def showdown(self):
        pass
