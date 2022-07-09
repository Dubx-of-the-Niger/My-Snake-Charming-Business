import random
print('You have 2 tries to guess the number.')
print()
mynum=int(input('Guess the number (1-5) :\n'))
num=[1,2,3,4,5]
cnum=random.choice(num)
for i in range(1,2):
    if mynum==cnum:
        print('You guessed it')
        break
    else:
        print('Try again!')
        mynum = int(input('Guess the number (1-5) :\n'))
if mynum!=cnum:
        print('You lose.')
        print('The number was {}'.format(cnum)+'.')
else:
    print('Congratulations!\nYou guessed the right number.')

2