print('This is a summation.')
total=0
a=int(input('Enter a number :'))
b=int(input('Enter another number :'))
total=a+b
ans=input('Do you want to add another number (y or n)\n')
while ans=='y':
    c=int(input('Enter the number:'))
    total=total+c
    print('The total is', total)
    print()
    ans = input('Do you want to add another number (y or n)\n')
print('The total is',total)