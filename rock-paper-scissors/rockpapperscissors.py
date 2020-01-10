import random

rand_choice = random.randint(1,3)

with open('text.txt') as text:
    rocktext = text.read()
print(rocktext)

if rand_choice == 1:
    rand_choice = 'rock'
    user_choice = str(input())
    wait_num = 0
    if user_choice == 'scissors' or 'paper':
        print('AI picks, ' + rand_choice)
        if user_choice == 'paper':
            print('\nyou win!')
        elif user_choice == rand_choice:
            print('\nITS A TIE!')
        else:
            print('\nyou lose!')

if rand_choice == 2:
    rand_choice = 'paper'
    user_choice = str(input())
    if user_choice == 'rock' or 'scissors':
        print('AI picks, ' + rand_choice)
        if user_choice == 'scissors':
            print('\nyou win!')
        elif user_choice == rand_choice:
            print('\nITS A TIE!')
        else:
            print('\nyou lose!')
        
if rand_choice == 3:
    rand_choice = 'scissors'
    user_choice = str(input())
    if user_choice == 'rock' or 'paper':
        print('AI picks, ' + rand_choice)
        if user_choice == 'rock':
            print('\nyou win!')
        elif user_choice == rand_choice:
            print('\nITS A TIE!')
        else:
            print('\nyou lose!')
