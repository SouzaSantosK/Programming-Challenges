AUTONOMY = 12
time_spent = int(input())
avg_speed = int(input())

distance = avg_speed * time_spent

liters = distance / AUTONOMY

print(f"{liters:.3f}")
