name=input("What's your firstname?")
if len(name) < 5:
    sur=input("What's your surname?")
    print('Welcome',str.upper(sur),str.upper(name))
else:
    print('Welcome',str.lower(name))