from player import Player
from deck import Deck

player1 = Player("Fines")
player2 = Player("Ferb")
deck = Deck()
deck.shuffle()

player1.pulling(deck)
player2.pulling(deck)
print(player1.info())
print(player2.info())
player2.throw()
print(player2.info())