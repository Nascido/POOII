from random import shuffle


class Member:
    def __init__(self) -> None:
        self._id = ''
        self._hand = ['']

    def comprarCarta(self, deck):
        carta = deck.retirarCarta()
        self._hand.append(carta)

    def jogarCarta(self, indexCarta):
        return self._hand.pop(indexCarta)


class Deck:
    def __init__(self, decks=1, joker=False, tipo="normal"):
        super().__init__()
        self._nipes = ['♠', '♣', '♥', '♦']
        self._num = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self._deck = []
        self._joker = joker
        self._tipo = tipo
        self._numberOfDecks = decks
        for i in range(decks):
            self._gerarDeck()

    def _gerarDeck(self):
        foradoTruco = ['8', '9', '10']
        for nipe in self._nipes:
            for num in self._num:
                if self._tipo == "espanhol":
                    if num not in foradoTruco:
                        self._deck.append((num, nipe))
                else:
                    self._deck.append((num, nipe))
        if self._joker:
            for i in range(2):
                self._deck.append("Joker")

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

    def get_number_of_cards(self):
        return len(self._deck)

    def get_number_of_decks(self):
        return self._numberOfDecks

    def __str__(self):
        cartas = len(self._deck)

        if self._joker:
            joker = "com"
        else:
            joker = "sem"

        return f"Baralho {self._tipo} {joker} coringa: {cartas} cartas"


class Player(Member):
    def getname(self):
        return self._id

    def __str__(self):
        return f"{self._id}: {self._hand}"


class Dealer(Member):
    pass


class Game:
    def __init__(self) -> None:
        self._game = None
        self._players = None

    def getplayers(self):
        return self._players

    def __str__(self):
        pass


class Table:
    pass


class Interface:
    pass
