from deck import Deck

class Player:
  def __init__(self, name):
    self.cards = []
    self.name = name

  def pulling(self, deck):
    card = deck.give()
    self.cards.append(card)

  def info(self):
    return "I {} with cards {}".format(self.name, ", ".join([card.info() for card in self.cards]))

  def throw(self):
    return self.cards.pop()
      
