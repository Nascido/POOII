
from random import shuffle


class Deck:
    def __init__(self, decks=1, blackjack=False):
        self._nipes = ['espadas', 'paus', 'copas', 'ouros']
        self._num = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self._deck = []
        self._numberOfDecks = decks
        for i in range(decks):
            self._gerarDeck(blackjack)

    def _gerarDeck(self, blackjack):
        for nipe in self._nipes:
            for num in self._num:
                self._deck.append(Card(num, nipe, blackjack))

    def embaralhar(self):
        shuffle(self._deck)

    def retirarCarta(self):
        return self._deck.pop(0)

    def devolverCarta(self, carta):
        self._deck.append(carta)

    def distribuir(self, players, handsize):
        tamcards = len(players)*handsize
        tamdeck = len(self._deck)

        if tamdeck >= tamcards:
            self.embaralhar()
            for i in range(handsize):
                for player in players:
                    player.comprarCarta(self)
        else:
            raise ValueError("Número de cartas do deck insuficiente!")

    def getdeck(self):
        return self._deck

    def __len__(self):
        return len(self._deck)

    def __str__(self):
        return f"{self._numberOfDecks} deck(s)"


class Card:
    def __init__(self, tipo, nipe, blackjack=False, valor=None, altvalor=None, setalt=False):
        # Como identificar a carta
        self._tipo = tipo
        self._nipe = nipe

        # Qual o seu valor atribuido
        self._valorOriginal = valor
        self._valorAlternado = altvalor
        self._valor = None

        # Como ela está valendo
        self.__alt = setalt

        if self._valor is None:
            self.atribuirvalor(blackjack)

    def atribuirvalor(self, blackjack=False):
        valorCartaAlta = 10
        valorAlternativo = None
        if blackjack:
            match self._tipo:
                case "J":
                    valorComum = valorCartaAlta
                case "Q":
                    valorComum = valorCartaAlta
                case "K":
                    valorComum = valorCartaAlta
                case "A":
                    valorComum = valorCartaAlta
                    valorAlternativo = 1
                case _:
                    valorComum = int(self._tipo)

        else:
            match self._tipo:
                case "J":
                    valorComum = 11
                case "Q":
                    valorComum = 12
                case "K":
                    valorComum = 13
                case "A":
                    valorComum = 14
                    valorAlternativo = 1
                case _:
                    valorComum = int(self._tipo)

        self._valorOriginal = valorComum
        self._valorAlternado = valorAlternativo
        self.verifalt()

    def verifalt(self):
        if self.__alt:
            self._valor = self._valorAlternado
        else:
            self._valor = self._valorOriginal

    def shift(self):
        if self.__alt:
            self.__alt = False
            self.verifalt()
        else:
            if self._valorAlternado is not None:
                self.__alt = True
                self.verifalt()

        return self._valor

    # Getters
    def gettipo(self):
        return self._tipo

    def getnipe(self):
        return self._nipe

    def getvalor(self):
        return self._valor

    def getaltvalor(self):
        return self._valorAlternado

    def __int__(self):
        return self._valor

    def __str__(self):
        return f"{self._tipo} de {self._nipe} "
