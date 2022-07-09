name=input('Enter your name : ')
num=int(input('Enter the number of times you want your name displayed : '))
num=num+1
if num>= 10:
    for i in range (1,4):
        print('Too high')
else:
    for i in range(1,num):
        print(name)