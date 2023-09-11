from trab02 import Player, Game

p_rafael = Player("Rafael")
p_eduardo = Player("Eduardo")
p_marcelo = Player("Marcelo")
p_gabriel = Player("Gabriel")
p_vitor = Player("Vitor")
p_jose = Player("José")
p_maria = Player("Maria")
p_fernanda = Player("Fernanda")
p_joana = Player("Joana")

players = [p_rafael, p_eduardo, p_marcelo, p_gabriel, p_vitor, p_jose, p_maria, p_fernanda, p_joana]

jogatina = Game(players)
jogatina.start()
