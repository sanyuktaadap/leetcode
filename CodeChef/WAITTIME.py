# cook your dish here
T = int(input())

for i in range(T):
    K, X = input().split()
    K = int(K)
    X = int(X)
    K = K*7
    print(f'{K-X}')