# cook your dish here
T = int(input())

for i in range(T):
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    if X >= Y:
        print("Yes")
    else:
        print("No")
    