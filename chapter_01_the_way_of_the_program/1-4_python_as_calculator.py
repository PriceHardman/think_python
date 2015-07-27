#   If you run a 10 kilometer race in 43 minutes 30 seconds, what is your average time per
#   mile? What is your average speed in miles per hour? (Hint: there are 1.61 kilometers in
#   a mile).

distance_traveled_in_km = 10 #10 km
time_in_minutes = 43.5

average_speed_in_kph = distance_traveled_in_km/(time_in_minutes/60)
average_speed_in_mph = average_speed_in_kph/1.61

print("Traveling",distance_traveled_in_km,"km in",time_in_minutes,"minutes equates to",average_speed_in_mph,"mph.")
