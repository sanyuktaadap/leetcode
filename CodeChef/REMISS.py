# cook your dish here
T = int(input())

for i in range(T):
    A, B = input().split()
    A = int(A)
    B = int(B)
    count_min = max(A, B)
    count_max = A + B
    print(f'{count_min} {count_max}')