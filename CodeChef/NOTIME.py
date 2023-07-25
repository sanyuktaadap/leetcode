# cook your dish here
inp = [int(i) for i in input().split()]
# N = inp[0]
H = inp[1]
x = inp[2]

time_zones = [int(i) for i in input().split()]

c = 0
for i in time_zones:
    if x + i >= H:
        c += 1

if c >= 1:
    print("Yes")
else:
    print("No")
    

    
    
    