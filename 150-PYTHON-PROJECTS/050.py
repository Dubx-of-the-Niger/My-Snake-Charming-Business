num=int(input('Enter a number between 10 and 20:'))
while num<10 or num>20:
    if num<10:
        print('Too low.\nTry again.')
        print()
        num = int(input('Enter a number between 10 and 20:'))
    elif num>20:
        print('Too high.\n Try again.')
        print()
        num = int(input('Enter a number between 10 and 20:'))
    else:
        print('Thank you')
print('Thank you')
