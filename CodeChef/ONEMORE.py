# cook your dish here
T = int(input())

for i in range(T):
    X = int(input())
    if X < 24:
        print("No")
    if X > 24:
        print("Yes")
    if X == 24:
        print("No")