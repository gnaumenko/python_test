Username = "Roman"
print ("Hello, " + Username + "! This is for you!")
print("Hello, {}! This is for you!".format(Username))
Message = "This is {user}!".format(user=Username)
print(Message)
text = "SoMe strIng"
print text.upper()
print text.lower()
print text.split(" ")
print text.split("o")

myBool = True
if myBool:
    print("Hello")
else:
    print("ooo")
my_list = [2, 23, 16.5, -3]
a = my_list[3]*2 + my_list[0]
print(a)
my_list.append(4)
print(my_list)
my_list.insert(0, 100)
print(my_list)
my_list = range(-10, 31, 3)
print(my_list)
print(len(my_list))

my_list = [1,17,0,5]
for x in my_list:
    print(x)
my_list = "Hello"
for x in my_list:
    print(x)

x = 0
while x != 10:
    print("something")
    x += 1
