from trab02 import Player, Deck


baralho = Deck()

p_rafael = Player("Rafael")
p_eduardo = Player("Eduardo")
p_marcelo = Player("Marcelo")
p_tobias = Player("Tobias")
p_gabriel = Player("Gabriel")

players = [p_rafael, p_eduardo, p_marcelo, p_tobias, p_gabriel]

baralho.distribuir(players, 2)
