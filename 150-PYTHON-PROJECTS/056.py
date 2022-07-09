import random
print('Guess the random number from 1 to 10:\n')
num=int(input('Enter your guess :\n'))
nums=[1,2,3,4,5,6,7,8,9,10]
cnum=random.choice(nums)
while num!=cnum:
    print('No,try again.')
    num = int(input('Enter your guess :\n'))
print('Thats the one.')