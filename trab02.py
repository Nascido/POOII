"""
    POOII - Trabalho 02

    Deck de Cartas: programa em python que embaralha e distribui
    um baralho de cartas para nove jogadores diferentes.

"""


class Deck:
    def __init__(self):
        self._nipes = ['♠', '♣', '♥', '♦']
        self._num = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self._normalDeck = []

    def gerarDeck(self):
        for nipe in self._nipes:
            for num in self._num:
                self._normalDeck.append((num, nipe))

class Player:
    pass


class Game:
    pass

