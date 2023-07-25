city = ""
temp = 201

def processeInput(tempCity, temp2):
    global city, temp
    temp2 = int(temp2)
    if temp2 < temp:
        temp = temp2
        city = tempCity

while True:
    [tempCity, temp2] = input().split()
    if tempCity == "Waterloo":
        processeInput(tempCity, temp2)
        break
    else:
        processeInput(tempCity, temp2)
print(city)
