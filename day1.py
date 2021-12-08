# day 1 advent of code
total = 0
with open('inputday1.txt') as f:
    lines = f.readlines()
counter = 0
last_line = 1000000
line_counter = 0
A = 0
B = 0
C = 0
for line in lines:

    line_counter+=1
    if line_counter>=4:
        if ((int(lines[line_counter-4])+ int(lines[line_counter-3])+int(lines[line_counter-2])) < (int(lines[line_counter-3])+int(lines[line_counter-2])+int(lines[line_counter-1]))):
            counter+=1
    
print(counter)
print(line_counter)
