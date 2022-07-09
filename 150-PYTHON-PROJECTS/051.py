num=int(input('Enter number of bottles on the wall:'))
print("There are {} green bottles hanging on the wall,{} green bottles hanging on the wall,\nand if 1 green bottle should fall,\nhow many green bottles would be standing on the wall?\n".format(num,num))
count=num-1
ans=int(input())
while ans!=count:
    print('No,try again.')
    ans=int(input())
print("Correct!\nThere'll be {} green bottles hanging on the wall.".format(ans))