total=0
print('Enter 5 numbers')
print()
print()
for i in range(1,6):
    a=int(input('Enter a number :'))
    b=input('Do you want that number included? (yes or no)')
    if b=='yes':
        total=total+a
    else:
        total=total
    print()
print('Your total is',total)
