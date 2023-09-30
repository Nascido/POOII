
from games import Player, Game, Blackjack
from decks import Deck, Card

"""
    Sistema de Casino - POOII 
"""

baralho = Deck()

baralho.embaralhar()

carta = baralho.retirarCarta()
