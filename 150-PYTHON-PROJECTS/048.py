count=2
for i in range(1,count):
    count=0
    name=input('Who do you want to invite to the party?\n')
    print(name,'has now been invited to the party.')
    count=count+1
    print('You have invited',count,'people to the party.')
    print()
    q=input('Do you want to invite another person to the party (y or n)')
    while q=='y':
        name=input('Who else do you want to invite to the party?\n')
        print(name, 'has now been invited to the party.')
        count = count + 1
        print('You have invited', count, 'people to the party.')
        print()
        q = input('Do you want to invite another person to the party (y or n)')
    print('You have invited',count,'people to the party.')