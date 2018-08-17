season = float(input('input number: '))
#a = str
#if season in [1, 2, 12]:
#    print ('Winter')
#elif season in [3, 4, 5]:
#    print ('Spring')
#elif season in [6, 7, 8]:
#    print ('Summer')
#elif season in [9, 10, 11]:
#    print ('Autumn')
#else:
#    print ('O NOOO')

if season in range(1,3) or season == 12:
    print ('Winter')
elif season in range(3,6):
    print ('Spring')
elif season in range(6,9):
    print ('Summer')
elif season in range(9,12):
    print ('Autumn')
#elif season == a:
#    print ('O')
else:
    print ('Enter correct number')

