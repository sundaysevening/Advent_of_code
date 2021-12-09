# day 3 advent of code
import statistics
with open('inputday3.txt') as f:
    lines = f.readlines()
    
    
output = ""
i=0
while (i< len(lines[0])-1):
    
    output+=(str(round(statistics.median([int(row[i]) for row in lines]))))
    i+=1
print(int(output,2))
print(int(output, 2)*((2**12-1)-int(output, 2)))
