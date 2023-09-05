"""
    POOII - Trabalho 02

    Deck de Cartas: programa em python que embaralha e distribui
    um baralho de cartas para nove jogadores diferentes.

"""
from random import shuffle


class Deck:
    def __init__(self, decks=1, jokers=False, truco=False):
        self._nipes = ['♠', '♣', '♥', '♦']
        self._num = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self._deck = []
        self._joker = jokers
        self._truco = truco
        self.gerarDeck(jokers, truco)

    def gerarDeck(self, jokers, truco):
        foradoTruco = ['8', '9', '10']
        for nipe in self._nipes:
            for num in self._num:
                if truco:
                    if num not in foradoTruco:
                        self._deck.append((num, nipe))
                else:
                    self._deck.append((num, nipe))
        if jokers:
            for i in range(2):
                self._deck.append("Joker")

    def embaralhar(self):
        shuffle(self._deck)

    def distribuir(self, players, handsize):
        tamcards = len(players)*handsize
        tamdeck = len(self._deck)

        if tamdeck >= tamcards:
            pass
        else:
            print("")





class Player:
    pass


class Game:
    pass
