
from decks import Deck
from games import Player

"""
    Sistema de Casino - POOII 
"""

baralho = Deck(blackjack=True)

player1 = Player("Rafael", 200)
player2 = Player("Tobias", 200)
player3 = Player("Rodrigo", 200)

players = [player1, player2, player3]

dealer = Player("Dealer", 1000)
