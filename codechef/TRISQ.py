# from sys import stdin
# lines = [line.rstrip('\n') for line in stdin]

chef = 'codechef/TRISQ_test.txt'
lines = [int(line.rstrip('\n')) for line in open(chef)]

print(lines)

T = lines[0]
C = lines[1:]
print(T,C)

# from math import fmod, floor
AnsList = []

for i in range(T):
    if C[i] <=3:
        fx = 0
    else:
        gx = int(0.5*(C[i]-2))
        fx = int(0.5*gx*(gx+1))
    AnsList.append(fx)

print(AnsList)
