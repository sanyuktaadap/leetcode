# cook your dish here
T = int(input())

for i in range(T):
    N = input()
    if N[:] == N[::-1]:
        print("wins")
    else:
        print("loses")
    
    