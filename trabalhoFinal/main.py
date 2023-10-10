
from decks import Deck
from games import Player

"""
    Sistema de Casino - POOII 
"""

baralho = Deck()
baralho.shuffle()

player1 = Player("Rafael")
player2 = Player("Tobias")

baralho.distribuir([player1, player2], 11)
