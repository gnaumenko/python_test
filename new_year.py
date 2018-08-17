def is_leap_year(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print ("{} Yes".format(year))
    else:
        print ("{} No".format(year))

def number_in_sq(number):
    return number**2
x = number_in_sq(5)
print x


is_leap_year(2000)
#for x in range (2000, 2012):
#    print('before')
#     leap_year(x)
#     print('after')