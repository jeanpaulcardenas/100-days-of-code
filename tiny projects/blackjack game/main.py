import random


def create_deck():
    cards = [x for x in range(1, 10)] + [10, 10, 10, 10]
    deck = cards * 4
    return deck


def deal_one_card(deck):
    """ Picks a card from 'deck' and returns it. deck is modified (new deck does not contain picked card)"""
    rand_int = random.randint(0, len(deck) - 1)
    print(len(deck))
    card_turned = deck[rand_int]
    deck.pop(rand_int)
    print(deck)
    return card_turned


def hand_dealing(deck):
    all_cards_handed = [deal_one_card(deck) for _ in range(4)]
    print(all_cards_handed)

    cards_dealt = {
        'dealers_cards': all_cards_handed[0:2],
        'players_cards': all_cards_handed[2:]
    }
    return cards_dealt


def win_message():
    print('U won')


