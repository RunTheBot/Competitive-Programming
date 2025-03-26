# Read input
start_time = input()
hour = int(start_time[:2])
minute = int(start_time[3:])

# Simulate travel
travel_time = 0
curr_hour = hour
curr_minute = minute

while travel_time < 120:  
    if (7 <= curr_hour < 10) or (15 <= curr_hour < 19):
        travel_time += 0.5 
    else:
        travel_time += 1
    
    curr_minute += 1
    if curr_minute == 60:
        curr_minute = 0
        curr_hour += 1
        if curr_hour == 24:
            curr_hour = 0

print(f"{curr_hour:02d}:{curr_minute:02d}")
