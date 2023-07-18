n = int(input())
T = 0
x = {"Poblano":1500, "Mirasol": 6000, "Serrano": 15500, "Cayenne":40000, "Thai":75000, "Habanero":125000}
for i in range(0, n):
    T = T + x[input()]
print(T)
