# cook your dish here
T = int(input())

for i in range(T):
    A, B = input().split()
    A = int(A)
    B = int(B)
    if (A + B) % 2 == 0:
        print("YES")
    else:
        print("NO")