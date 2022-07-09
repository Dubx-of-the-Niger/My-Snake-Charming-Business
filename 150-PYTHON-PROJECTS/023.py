poem=input('start a nursery ryhme:')
print('The length of that line is',len(poem),'letters.')
print()
q=input('Want to see something fun? (yes or no)')
if q=='yes':
    a = int(input("Where should we start?"))
    b = int(input('Where should we end?'))
    print('''That portion is "''', poem[a:b], '''"''')
else:
    print('Daz all.')