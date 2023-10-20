time = int(input())

hours = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time

# stamps = [0 for _ in range(3)]

# while time != 0:
#     if time >= 3600:
#         stamps[0] += time // 3600
#         time -= stamps[0] * 3600
#     elif time >= 60:
#         stamps[1] += time // 60
#         time -= stamps[1] * 60
#     else:
#         stamps[2] += time
#         time -= stamps[2]
# print(f"{stamps[0]}:{stamps[1]}:{stamps[2]}")

print(f"{hours}:{minutes}:{seconds}")
