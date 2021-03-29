n = int(input())
tmp = []

for _ in range(n):
    (x,y) = input().split(" ")
    tmp.append([x,y])

tmp = sorted(tmp, key = lambda x : int(x[0]))

for i in tmp:
    print(i[0],i[1])