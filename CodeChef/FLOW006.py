T = int(input())

for i in range(T):
    num = input()
    
    sum = 0
    for j in range(len(num)):
        sum = sum + int(num[j])
    
    print(sum)