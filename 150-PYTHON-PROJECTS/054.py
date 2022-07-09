import random
print('You must match computers choice to win.')
me=input('Choose heads or tails :')
comp=['heads','tails']
win=random.choice(comp)
if me==win:
    print()
    print('You win!\nYou guessed right.')
else:
    print()
    print('You lose.\nComputer chose {}'.format(win)+'.')