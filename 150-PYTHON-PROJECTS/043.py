dirr=input('Which direction do you want to count (up or down)')
if dirr=='up':
    a=int(input('Enter the top number : '))
    a=a+1
    for i in range(1,a):
        print(i)
elif dirr=='down':
    a=int(input('Enter a number below 20 :'))
    a=a-1
    for i in range(20,a,-1):
        print(i)
else:
    print('I dont understand. Bye.')

