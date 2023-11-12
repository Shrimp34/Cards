class Card:
  def __init__(self, suit, val):
    self.suit = suit
    self.val = val

  def info(self):
    if self.val == 1:
      val = "Tuz"
    elif self.val == 11:
      val = "Valet"
    elif self.val == 12:
      val = "Dama"
    elif self.val == 13:
      val = "korol"
    else:
      val = self.val
    return "{} of {}".format(val, self.suit)