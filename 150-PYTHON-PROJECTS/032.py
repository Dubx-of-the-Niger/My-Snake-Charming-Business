import math
pi=math.pi
rad=int(input('Enter the radius of the cylinder:'))
depth=int(input('Enter the depth of the cylinder:'))
area=(rad**2)*pi
volume=area*depth
volume=round(volume,3)
print('The volume of the cylinder is',volume)