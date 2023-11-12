from card import Card
import random
class Deck:
  def __init__(self):
    self.cards = []
    self.create()

  def info(self):
    for card in self.cards:
      print(card.info())

  def create(self):
    self.suits = ["piki", "chervi", "bibny", "trefi"]
    for suit in self.suits:
      for val in range(1, 14):
        self.cards.append(Card(suit, val))

  def shuffle(self):
    random.shuffle(self.cards)

  def give(self):
    return(self.cards.pop())
