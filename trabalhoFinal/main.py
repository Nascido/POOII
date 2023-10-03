
from decks import Deck

"""
    Sistema de Casino - POOII 
"""

baralho = Deck(blackjack=True)

baralho.embaralhar()

card = baralho.retirarCarta()
