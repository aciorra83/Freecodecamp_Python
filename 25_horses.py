#number function is prefered method for generating random lists of integers

##list_numbers = []
##
##for i in range(3):
##    list_numbers.append(list(range(1,6)))

##shuffle(x, random=None) method of random.Random instance
##    Shuffle list x in place, and return None.

import random

##number = [random.randint(1,5) for i in range(10)]
##

##step 1 get a list with range 1:25
numbers = [i for i in range(1,26)]

##step 2 shuffle the list (iterable items)
random.shuffle(numbers)

##step 3 spread out over sub lists
shuffled = [13, 1, 11, 6, 12,
            16, 23, 18, 20, 4,
            25, 17, 21, 8, 5,
            9, 10, 3, 24, 19,
            15, 14, 2, 22, 7]

horses = [[],
          [],
          [],
          [],
          [],
    ]

##for i in range(5):
##    for j in range(5):
##        horses[j].append(shuffled.pop())
    
horses = [[7, 19, 5, 4, 12],
          [22, 24, 8, 20, 6],
          [2, 3, 21, 18, 11],
          [14, 10, 17, 23, 1],
          [15, 9, 25, 16, 13]]

##sort(*, key=None, reverse=False) method of builtins.list instance
##    Sort the list in ascending order and return None.
for race in horses:
    race.sort()
    
for race in horses:
    print(race)

def last(x):
    return x[-1]

##setting reverse to true puts teh fastest horse at [-1]
new_horses = sorted(horses,key=last,reverse=True)
print()
for race in new_horses:
    print(race)
    
## output is:
## [9, 13, 15, 16, 25]
## [6, 8, 20, 22, 24]
## [1, 10, 14, 17, 23]
## [2, 3, 11, 18, 21]
## [4, 5, 7, 12, 19]



