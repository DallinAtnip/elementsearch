'''
a function that takes an ordered list of numbers (a list where the elements are in order from
smallest to largest) and another number. The function decides whether or not the given number
is inside the list and returns (then prints) an appropriate boolean.
Dallin Atnip 6/1/19
'''
#copied from here v
def binarySearch (arr, l, r, x): 
  
    if r >= l: 
  
        mid = l + (r - l) // 2
  
        if arr[mid] == x: 
            return mid 
          
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        else: 
            return binarySearch(arr, mid+1, r, x) 
  
    else: 
        return -1
#copied to here ^

mylist = [0,2,4,6,8,10]
usernumber = int(input("pick a number 0-10: "))

result = binarySearch (mylist, 0, len(mylist)-1, usernumber)

if result != -1: 
    print ("Element is present at index %d" % (result,))
else: 
    print ("Element is not present in array")

'''
if usernumber == 0 or 2 or 4 or 6 or 8 or 10:
    print ("good boy")
else:
    print ("you suck")
'''
