"""
    POOII - Trabalho 02

    Deck de Cartas: programa em python que embaralha e distribui
    um baralho de cartas para nove jogadores diferentes.

"""
from random import shuffle


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


class Player:
    def __init__(self, nome, valorpote=0):
        self._name = nome
        self._hand = []
        self._pote = valorpote

    def apostar(self, valor):
        if valor <= self._pote:
            self._pote -= valor
            return True
        else:
            return False
        
    def recebeValor(self, valor):
        self._pote += valor

    def comprarCarta(self, deck):
        carta = deck.retirarCarta()
        self._hand.append(carta)

    def jogarCarta(self, indexCarta):
        return self._hand.pop(indexCarta)
    
    def getname(self):
        return self._name

    def __str__(self):
        return f"{self._name}: {self._hand}"


class Game:
    def __init__(self, jogadores=None, jogo="pife") -> None:
        self._game = jogo
        self._players = jogadores
        self._baralho = None

    def start(self):
        if self._game == "pife":
            self.jogarPife()
            return True
        
        else:
            return False

    def registrarPlayer(self, nome):
        jogador = Player(nome)
        self._players.append(jogador)

    def removerPlayer(self, nome):
        self._players.pop(nome)

    def jogarPife(self):
        if self._players is None:
            n = 0
        else:
            n = len(self._players)

        ready = False
        print("#################################################")
        print(f" {n} jogadores inscritos!\n")

        while not ready:
            if n < 5:
                i = 5-n
                print(f"Necessário adicionar mais {i} no mínino.")
                while i > 0:
                    nome = input(" - Nome: ")
                    self.registrarPlayer(nome)
                    i -= 1

            elif 5 <= n < 9:
                adicionar = input(f" Deseja adicionar mais algum? ")
                if adicionar == 'y':
                    nome = input(" - Nome: ")
                    self.registrarPlayer(nome)
                
                else:
                    ready = True
            
            elif n == 9:
                print(f"Número máximo de jogadores, o jogo pode começar!\n")
                ready = True
            
            else:
                print(f"\nNúmero máximo de jogadores excedido!")
                i = n-9
                print("#################################################")
                print(f"Remova {i} jogador(es) de sua escolha!\n")
                while n > 9:
                    for player in self._players:
                        print(f"{player.getname} - {i}")

                    option = int(input(" - Nome para retirar: "))
                    self.removerPlayer(self._players[option-1])
                    n -= 1

            n = len(self._players)

        self._deck = Deck(decks=2)
        self._deck.distribuir(self._players, 9)

    def getdeck(self):
        return self._deck.getdeck()

    def __str__(self):
        n = len(self._players)
        i = self._deck.get_number_of_decks()
        return f"Jogo {self._game}: {n} pessoas e {i} deck(s)"
