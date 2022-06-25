import secrets
import string

# print("".join(secrets.choice(string.digits + string.ascii_letters + string.punctuation)
#               for i in range(100)))
#

# x = 0
# while x < 100:
#     x += 1
#     print(x)

# mylist = [1, 2, 3]
# mylist2 = [1, 2, 3]

# with open('c:/test/test.txt', 'r') as textfile:
#     for item in textfile:
#         print(item)


# for item in mylist:
#     print(item)

# print(len(mylist))
#
# print(len(mylist) + len(mylist))

import itertools as it
import collections as ct

import pandas as pd
names = ['ll', 'll', 'hl', 'hl', 'LL', 'LL', 'LL', 'HL', 'll']



codes, uniques = pd.factorize(names)
codes