# cook your dish here
T = int(input())

for i in range(T):
    N, K = input().split()
    N = int(N)
    K = int(K)
    money = ""
    A = input().split()
    # A = A.split()
    a = [int(i) for i in A]
    for x in a:
        if  x <= K:
            money += '1'
            K -= x
        else:
            money += '0'
    print(money)