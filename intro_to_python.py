'''
numbers = [1, -5, 2,-4, 0, 6, 10, 3]
#utilize elif to check the first if and exterminate from there
for number in numbers:
    if number == 0:
        print("zero")
    elif number > 0:
        print("positive")
    else:
        print("negative")
'''
'''
def even(x):
    """Enter a number to be checked if even""" #this is docstring
    if x % 2 == 0:
        return True
'''
'''
#this is the more efficient way to run the above code
def even(x):
    return x % 2 == 0
def odd(y):
    return y % 2 != 0
print(even(4))
'''


for row in range(5):

    #print(row)
    for col in range(5):
        print(col, end="")
    print()

