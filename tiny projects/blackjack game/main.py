import random


def create_deck():
    cards = [x for x in range(2, 10)] + [11, 10, 10, 10, 10]
    deck = cards * 4

    return deck


def deal_one_card(deck):
    """ Picks a card from 'deck' and returns it. deck is modified (new deck does not contain picked card)"""
    rand_int = random.randint(0, len(deck) - 1)
    print(len(deck))
    card_turned = deck[rand_int]
    deck.pop(rand_int)

    return card_turned


def hand_dealing(deck):
    all_cards_handed = [deal_one_card(deck) for _ in range(4)]
    print(all_cards_handed)

    cards_dealt = {
        'dealers_cards': all_cards_handed[0:2],
        'players_cards': all_cards_handed[2:]
    }
    return cards_dealt


def print_cards_during_game(player: list, dealer: list, all_cards: bool):
    if all_cards:
        return print(f'your cards {player}\n dealers hand {dealer}')
    return print(f'your cards {player}\n dealers hand [{dealer[0]}, ?]')


def check_cards_21(cards_to_check: list, player: bool, ):
    """cards to count, player is boolean"""
    if sum(cards_to_check) == 21:
        if player:
            print('Congrats, u won! ')
        else:
            print('house wins')
        return True

    else:
        return False


def ask_to_play_again() -> bool:
    """ask to play again. return True if 'Y' return False if 'N'"""
    want_to_play_again = ''

    while want_to_play_again not in ['Y', 'N']:
        want_to_play_again = input('\nWould you like to play again? Y/N').upper()
    if want_to_play_again == 'Y':
        return True
    else:
        return False


play = True
results = {
    True: 'Congrats bruh u won!',
    False: 'U lost man',
    'draw': 'its a draw'
}
while play:
    print('hi')
    want_to_play = ''
    player_win = 'draw'
    while want_to_play not in ['Y', 'N']:
        want_to_play = input('Ready? Y/N').upper()

    if want_to_play == 'N':
        play = False
        break
    # create deck
    my_deck = create_deck()
    # game start
    cards_dealt = hand_dealing(my_deck)
    dealers_hand = cards_dealt['dealers_cards']
    players_hand = cards_dealt['players_cards']

    print_cards_during_game(players_hand, dealers_hand, all_cards=False)
    game_over = False
    if check_cards_21(players_hand, player=True):
        play = ask_to_play_again()
        continue

    keep_asking = True
    while keep_asking and not game_over:
        request_card = input(f'deal? Y/N').upper()

        if request_card == 'Y':
            print('another card has been dealt')
            players_hand.append(deal_one_card(my_deck))
            if check_cards_21(players_hand, player=True):
                game_over = True
                player_win = True

            if sum(players_hand) > 21:
                if 11 in players_hand:
                    players_hand.remove(11)
                    players_hand.append(1)

                else:
                    game_over = True
                    player_win = False
            print_cards_during_game(players_hand, dealers_hand, False)

        else:
            keep_asking = False

    if not game_over:
        while sum(players_hand) >= sum(dealers_hand) < 17:
            print_cards_during_game(players_hand, dealers_hand, True)
            dealers_hand.append(deal_one_card(my_deck))
            if sum(dealers_hand) > 21 and 11 in dealers_hand:
                dealers_hand.remove(11)
                dealers_hand.append(1)

        if sum(players_hand) > sum(dealers_hand) or sum(dealers_hand) > 21:
            player_win = True

        elif sum(players_hand) < sum(dealers_hand):
            player_win = False

    print_cards_during_game(players_hand, dealers_hand, True)
    print(results[player_win])
    if not ask_to_play_again():
        play = False

