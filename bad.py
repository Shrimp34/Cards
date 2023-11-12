import random

# Определение карты
def create_card(suit, value):
    card = {
        "suit": suit,
        "value": value
    }
    return card

# Отображение карты
def show_card(card):
    val = card["value"]
    if val == 1:
        val = "Туз"
    elif val == 11:
        val = "Валет"
    elif val == 12:
        val = "Дама"
    elif val == 13:
        val = "Король"

    return "{} {}".format(val, card["suit"])

# Создание колоды
def create_deck():
    deck = []
    suits = ['Черви', 'Трефы', 'Бубны', 'Пики']
    for suit in suits:
        for val in range(1, 14):
            deck.append(create_card(suit, val))
    return deck

# Перемешивание колоды
def shuffle_deck(deck, num=1):
    for _ in range(num):
        random.shuffle(deck)

# Выдача верхней карты
def deal_card(deck):
    return deck.pop()

# Создание игрока
def create_player(name):
    player = {
        "name": name,
        "hand": []
    }
    return player

# Приветствие игрока
def say_hello(player):
    print("Привет! Меня зовут {}".format(player["name"]))

# Вытягивание карт игроком
def draw_card(player, deck, num=1):
    for _ in range(num):
        card = deal_card(deck)
        if card:
            player["hand"].append(card)
        else:
            return False
    return True

# Отображение руки игрока
def show_hand(player):
    print("{}'s рука: {}".format(player["name"], [show_card(card) for card in player["hand"]]))

# Сброс карты игроком
def discard_card(player):
    return player["hand"].pop()

# Тестирование
my_deck = create_deck()
shuffle_deck(my_deck)

bob = create_player("Боб")
say_hello(bob)
draw_card(bob, my_deck, 5)
show_hand(bob)