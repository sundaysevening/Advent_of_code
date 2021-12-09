# day 3 advent of code
import statistics
import copy
with open('inputday3.txt') as f:
    lines = f.readlines()
    
lines2 = copy.deepcopy(lines)

i=0
while (len(lines)>1 and i< 12):
    
    mostcommon=(str(int(statistics.median([int(row[i]) for row in lines])>0)))
    temp = [line for line in lines if line[i] == mostcommon]
    lines = temp.copy()
    i+=1


oxygen = lines[0]

i=0
while (len(lines2)>1 and i< 12):
    mostcommon=(str(int(statistics.median([int(row[i]) for row in lines2])>0)))
    temp = [line for line in lines2 if line[i] != mostcommon]
    lines2 = temp.copy()
    i+=1
    
co2 = lines2[0]

print(int(oxygen,2)*int(co2,2))