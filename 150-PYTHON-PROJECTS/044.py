num=int(input('How many people do you want to invite to your party?\n'))
if num<=10:
    num=num+1
    for i in range(1,num):
        inv=input('Who would you like to invite?\n')
        print(inv,'has been invited.')
        print()
else:
    print('Too many people.')