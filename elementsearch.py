'''
a function that takes an ordered list of numbers (a list where the elements are in order from
smallest to largest) and another number. The function decides whether or not the given number
is inside the list and returns (then prints) an appropriate boolean.
Dallin Atnip 6/1/19
'''
mylist = [0,2,4,6,8,10]

usernumber = int(input("pick a number 0-10: "))


if usernumber == 0 or 2 or 4 or 6 or 8 or 10:
    print ("good boy")
else:
    print ("you suck")

