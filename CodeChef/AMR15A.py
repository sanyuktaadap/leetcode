# cook your dish here
T = int(input())

lucky = 0
unlucky = 0

# for i in range(T):
weapons = input().split()
for weapon in weapons:
    weapon = int(weapon)
    if weapon % 2 == 0:
        lucky += 1 
    else:
        unlucky += 1

if lucky > unlucky:
    print("READY FOR BATTLE")
else:
    print("NOT READY")