change = int(input())
print("All positions change in year", change)

for i in range((int(input())-change)//60):
    print("All positions change in year", change+60*(i+1))

