# cook your dish here
T = int(input())

for i in range(T):
    features = [int(y) for y in input().split()]
    f = [features[0], features[1]]
    rev_f = list(reversed(f))
    # rev_f = [features[1], features[0]]
    p1 = [features[2], features[3]]
    p2 = [features[4], features[5]]
    
    if (f == p1) or (rev_f == p1):
        print(1)
    elif (f == p2) or (rev_f == p2):
        print(2)
    else:
        print(0)