
from games import Player, Poker

"""
    Sistema de Poker - POOII 
"""

player1 = Player("Rafael", 1000)
player2 = Player("Éric", 1000)
player3 = Player("Carioca", 1000)

players = [player1, player2, player3]

pokergame = Poker(players)
pokergame.iniciar()