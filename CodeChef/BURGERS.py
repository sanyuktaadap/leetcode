# cook your dish here
T = int(input())

for i in range(T):
    a, b = input().split()
    a = int(a)
    b = int(b)
    
    # if a > b:
    #     print(b)
    # else:
    #     print(a)
    
    print(min(a, b))