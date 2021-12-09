# day 2 advent of code
with open('inputday2.txt') as f:
    lines = f.readlines()
horizontal = 0
depth = 0
aim = 0
for line in lines:
    
    if "forward" in line:
        horizontal += int(line[-2])
        depth += (aim * int(line[-2]))
    elif "down" in line:
        aim += int(line[-2])
    elif "up" in line:
        aim -= int(line[-2])

print(horizontal)
print(depth)
print(depth * horizontal)
    