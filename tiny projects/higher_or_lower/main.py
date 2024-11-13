# print arte
import os
import random
from data import data as ig_data
from art import logo as logo_art, vs as vs_art


# current score, data copy, game_over. random pick y pop item 2 veces. elegir entre los 2 (input) while not
# game_over, si data[index][follower_count] elegido es mayor al no elegido sumar +1 a score y eliminar opcion 1,
# opcion 2 pasa a ser opcion 1 y opcion 2 es randompick.
# si game_over print(sorry, that's wrong, final score: x)


def higher_or_lower(my_data, my_logo, my_vs):
    data = my_data.copy()
    logo = my_logo
    vs = my_vs
    score = 0
    game_over = False
    txt = '{name}, a {description}, from {country}'

    def account(ig_datas: list) -> dict:
        index = random.randint(0, len(ig_datas) - 1)
        pick = ig_datas.pop(index)
        return pick

    a = account(data)
    while not game_over:
        print(logo)

        b = account(data)

        followers = {
            'a': a['follower_count'],
            'b': b['follower_count']
        }
        if score > 0:
            print(f'You are right: current score: {score}')
        print(f'Compare A: {txt.format(**a)}\n\n'
              f'{vs}\n'
              f'Against B: {txt.format(**b)}')

        player_choice = input('').lower()
        print(f'\n' * 20)
        if followers[player_choice] is max(followers.values()):
            score += 1
            a = b.copy()
        else:
            print(f'{logo}\nSorry! wrong. Final score: {score}')
            game_over = True


higher_or_lower(ig_data, logo_art, vs_art)
