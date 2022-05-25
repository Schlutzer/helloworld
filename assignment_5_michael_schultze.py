'''
Blackjack
'''
import sys
import random
import time

print('Welcome to Blackjack')
print('-----------------------------------------------------------')
game_end = False
draw_card = 0
hit = ""
card_list = [1,2,3,4,5,6,7,8,9,10]
while not game_end:
    try:
        print()
        print()
        game_start = input('Do you wish to start a new game?(y/n):  ')
        print()
        print()
        player_card_1 = 0
        player_card_2 = 0
        player_total = 0
        dealer_card_1 = 0
        dealer_card_2 = 0
        player_stand = False
        dealer_stand = False
        player_bust = False
        dealer_bust = False
        if game_start == 'y':
            player_card_1 = random.choice(card_list)
            player_card_2 = random.choice(card_list)
            player_total = player_card_1+player_card_2

            dealer_card_1 = random.choice(card_list)
            dealer_card_2 = random.choice(card_list)
            dealer_total = dealer_card_1+dealer_card_2
            print('-----------------------------------------------------------')
            print()
            print(f' You draw {player_card_1} and {player_card_2}. You total is {player_total}')
            time.sleep(1)
            print()
            print(f' Dealer draws {dealer_card_1} and a hidden card.')
#Player loop
            while player_total <= 21 and not player_stand:
                try:
                    print()
                    hit = input('Hit or stand? (h/s) ')
                    if hit == 'h':
                        draw_card =random.choice(card_list)
                        player_total += draw_card
                        print(f'Hit! You draw {draw_card}. Your total is {player_total} ', end = '')
                    elif hit == 's':
                        print('You stand')
                        player_stand = True
                    else:
                        print('You must type h or s, try again')
                except ValueError:
                    print('try again')
            else:
                if player_stand is True:
                    print(f'Your total is {player_total}')
                else:
                    print(f'Your total is {player_total} BUST!')
                    print('Dealer Wins!')
                    player_bust = True

#Dealer loop
            if not player_bust:
                print()
                print(f'The dealer reveals their hidden card of {dealer_card_2}, ', end = '')
                print(f'for a total of {dealer_total}')
                while dealer_total <=17 and not dealer_stand:
                    draw_card = random.choice(card_list)
                    dealer_total += draw_card
                    print()
                    print(f'Hit! The dealer draws {draw_card}. Dealer total is {dealer_total}')
                    time.sleep(1)
                    if 17 <= dealer_total <= 21:
                        dealer_stand = True
                        print('The dealer stands')
                    elif dealer_total > 21:
                        print()
                        print(f'Dealer total is {dealer_total} BUST!')
                        print('You win')
                        dealer_bust = True
#end of the game logic
                if not dealer_bust:
                    print()
                    print(f'Your total is {player_total}, the dealer\'s total is {dealer_total}')
                    if dealer_total >= player_total:
                        print()
                        print('Dealer Wins!')
                    else:
                        print()
                        print('You win!')
        elif game_start == 'n':
            game_end = True
        elif game_start != 'y' or game_start != 'n' :
            print('You must type y or n, try again')
        else:
            game_end = True

    except ValueError:
        print('You must type y or n, try again')
    print()
    print('-----------------------------------------------------------')
print("Thank you for playing")
