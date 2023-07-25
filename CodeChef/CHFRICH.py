# cook your dish here
import math

T = int(input())

for i in range(T):
    money = [int(x) for x in input().split()]
    A = money[0]
    B = money[1]
    X = money[2]
    print(math.ceil((B - A) / X))