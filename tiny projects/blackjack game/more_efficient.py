from random import randint

DECK = (list(range(2, 12)) + [10, 10, 10]) * 4


def show_cards(hand_1: list, hand_2: list, all_cards: bool):
    if all_cards:
        print(f'your cards {hand_1}\ndealers cards {hand_2}')
    else:
        print(f'your cards {hand_1}\ndealers cards [{hand_2[0]}, ?]')


def deal(deck: list, hand: list):
    index = randint(0, len(deck) - 1)
    card = deck.pop(index)
    hand.append(card)
    if sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
    return card


def blackjack_game(deck_to_use):
    deck = deck_to_use.copy()
    game_over = False
    players_hand = []
    dealers_hand = []
    play = ''

    while play not in ['Y', 'N']:
        play = input('want to play?').upper()
    if play == 'N':
        quit()

    for _ in range(2):
        deal(deck, players_hand)
        deal(deck, dealers_hand)
        print(deck)

    player_score = sum(players_hand)
    dealer_score = sum(dealers_hand)

    show_cards(players_hand, dealers_hand, False)

    if player_score == 21 or dealer_score == 21:
        game_over = True
        show_cards(players_hand, dealers_hand, True)

    request_deal = ''
    while not game_over and request_deal != 'N' and player_score < 21:
        request_deal = input('request deal? Y/N').upper()

        if request_deal == 'Y':
            deal(deck, players_hand)
            player_score = sum(players_hand)
            show_cards(players_hand, dealers_hand, False)
            if player_score >= 21:
                game_over = True
    while not game_over and dealer_score < 17:
        show_cards(players_hand, dealers_hand, True)
        deal(deck, dealers_hand)
        dealer_score = sum(dealers_hand)

    show_cards(players_hand, dealers_hand, True)
    if player_score > 21 or player_score < dealer_score < 21:
        print('u lose')

    elif player_score == dealer_score:
        print('draw')

    else:
        print('u win')


start = True
while start:
    blackjack_game(DECK)
