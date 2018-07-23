import math
year = (input('input year: '))
if math.fmod(year, 4):
#if year % 4 != 0:
    print ("No")
else:
    print ("Yes")