import random
fruit=['apple','orange','paw-paw','mango','banana']
choice=random.choice(fruit)
for i in range (1,5):
    print(choice)
    choice = random.choice(fruit)