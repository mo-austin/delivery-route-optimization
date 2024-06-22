

import sys
import time
from Service import Service

fp = open("example.txt", 'r')
lines = fp.readlines()

# Parse the input
numCities = int(lines[0])
start = int(lines[1])
end = int(lines[2])
capacities = []
loads = []
capacitiesDone = False

for i in range(3, len(lines)):
    line = lines[i].strip()
    if line == "---":
        capacitiesDone = True
    elif not capacitiesDone:
        capacities.append(line)
    else:
        loads.append(line)
        
# Call method and print the result
startT = time.time()
f = Service()
output = f.compute(numCities, capacities, loads, start, end)
endT = time.time()
for city in output:
    print(city)
print("time: "+ str(endT-startT))
