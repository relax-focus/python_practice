import sys
from random import randint

# def roll_dice(n=2):
#     total = 0
#     for _ in range(n):
#         total += randint(1, 6)
#     return total

# def add(a=1, b=2, c=3):
#     return a + b + c

# def add(*args):
#     total = 0
#     for val in args:
#         total += val
#     return total

# print(roll_dice())
# print(roll_dice(3))

# print(add())

def gcd(x, y):
    """求最大公约数"""
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
        
def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x, y)

print("%d和%d的最大公约数是%d" % (3, 7, gcd(3, 7)))
print("%d和%d的最小公倍数是%d" % (3, 6, lcm(3, 6)))

input()