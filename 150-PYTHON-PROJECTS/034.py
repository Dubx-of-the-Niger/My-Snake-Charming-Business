a=int(input('     1) Square\n     2)Triangle \n\n     Enter a number : '))
if a==1:
    s=int(input('Enter the length of one side : '))
    area=s*2
elif a==2:
    s=int(input('Enter the base of the triangle : '))
    h=int(input('Enter the height of the triangle : '))
    area=0.5*s*h
else:
    print('You entered a wron number')
print('The area of that is',area)
