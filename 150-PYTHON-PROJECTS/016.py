rain=input('Is it rainy (yes or no):')
windy=input('Is it windy (yes or no):')
rain=str.lower(rain)
windy=str.lower(windy)
if rain == 'yes' and windy == 'yes':
    print("It's too windy for an Umbrella.")
elif rain == 'yes' and windy!= 'yes':
    print('Take an Umbrella.')
else:
    print('Enjoy your day!')