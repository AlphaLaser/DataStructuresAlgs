'''
USACO Bronze - 2019
Problem Statement: https://usaco.org/index.php?page=viewproblem2&cpid=891
'''

# input parsing
raw = int(input())
inp = []

for i in range(raw):
    x = input()
    inp.append(list(map(int, x.split())))

result = 0

for j in range(3):
    count = 0
    shell = [0, 0, 0]
    shell[j] = 1

    for i in inp:
        shell[i[0] - 1], shell[i[1] - 1] = shell[i[1] - 1], shell[i[0] - 1]
        if shell[i[2] - 1] == 1:
            count += 1

    if count > result:
        result = count

print(result)



