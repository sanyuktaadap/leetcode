# cook your dish here
import math

T = int(input())

for j in range(T):
    N = int(input())
    
    if N == 1:
        print('no')
        continue
    
    #bool flag to check if we enter the if cond or not
    prime = True
    
    for i in range(2, int(math.sqrt(N) + 1)):
        if N % i == 0:
            prime = False
            break
        
    if prime:
        print('yes')
    else:
        print('no')
        
    