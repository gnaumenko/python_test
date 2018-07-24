#import math
#if math.fmod(year, 4):
#if year % 4 != 0:
#    print ("No")
#else:
#    print ("Yes")
year = (input('input year: '))
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print ("Yes")
elif year % 100 == 0 and year % 400 != 0:
    print ("No")
elif year % 100 == 0:
    print ("No")