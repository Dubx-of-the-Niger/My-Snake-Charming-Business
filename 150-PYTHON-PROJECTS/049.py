mynum=50
count=0
yournum=int(input('Guess the number'))
while mynum!=yournum:
    if yournum<mynum:
        print("That's too low")
    else:
        print("That's too high.")
    count=count+1
    yournum=int(input('Guess again.'))
print('You guessed it in',count,'tries.')