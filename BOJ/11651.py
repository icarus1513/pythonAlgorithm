n=int(input())
arr=[]

for _ in range(n):
    (x,y)= list(map(int,input().split()))
    arr.append((x,y))


arr=sorted(arr, key = lambda x : x[1])

for i in arr:
    print(i[0], i[1])