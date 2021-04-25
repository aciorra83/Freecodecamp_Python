'''
numbers = [1, -5, 2, -4, 0, 6, -10, 3]

def Pos_Neg(x):
    if number == 0:
        print("Zero")
    else:
        if number > 0:
            print("Positive")
        else:
            print("Negative")

for number in numbers:
    #print(number)
    Pos_Neg(number)
'''

'''
#number triangle exercise
for row in range(1, 11):
    for col in range(1, row+1):
        print(col, end="")
    print()
'''

'''
for row in range(1,14):
    for col in range(1, row+1):
        print('{:3}'.format(col),end="")
    print()
'''
#the first way I learned this function
'''
def hello():
    name = input("Enter name: ")
    print("Hello " + name + "nice to meet you.")
hello()
'''

'''
#this way uses the .format() built-in function
def hello():
    name = input("Enter name: ")
    print("Hello {} nice to meet you.".format(name))
hello()
'''

#number = int(input("Enter a number: "))
#print(type(number))

'''
#Blastoff exercise that uses while loop
count = int(input("Enter a number: "))
print("Ready")
while count >= 0:
    print(count)
    count -= 1
print("Blast offffff!!!!")
'''

numbers = [1, -5, 2, -4, 0, 6, -10, 3]
'''
pos = []
neg = []
for number in numbers:
    if number > 0:
        pos.append(number)
    else:
        neg.append(number)
print(pos)
print(neg)
'''

pos = [i for i in numbers if i > 0]
print(pos)