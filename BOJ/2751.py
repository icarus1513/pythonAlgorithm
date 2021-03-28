n = int(input())
arr = []
for i in range(n):
    inp = input()
    arr.append(inp)

arr.sort()
for i in arr:
    print(i)