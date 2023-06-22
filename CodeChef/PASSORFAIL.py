# cook your dish here
T = int(input())

for i in range(T):
    N, X, P = input().split()
    N = int(N)
    X = int(X)
    P = int(P)
    marks = (X * 3) - (N - X)
    
    if marks >= P:
        print("PASS")
    else:
        print("FAIL")
        
    
    