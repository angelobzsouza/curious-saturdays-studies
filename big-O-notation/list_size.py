import random
import time

LIST_SIZE = 60000000

randomlist = []
for i in range(0, LIST_SIZE):
    n = random.randint(10, 30)
    randomlist.append(n)

before_time = time.time()

max = 0
for number in randomlist:
    max = number if number > max else max

min = 999999
for number in randomlist:
    min = number if number < min else min

print(time.time() - before_time)

before_time = time.time()
max = 0
min = 999999
for number in randomlist:
    max = number if number > max else max
    min = number if number < min else min

print(time.time() - before_time)
