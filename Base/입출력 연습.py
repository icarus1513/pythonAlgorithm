## BOJ 10952
while True:
    tmp =  list(map(int,input().split()))
    if tmp[0]== 0 and tmp[1] == 0:
        break
    print(int(tmp[0])+int(tmp[1]))


##BOJ 10953
n = int(input())
for i in range(n):
    tmp = list(map(int, input().split(",")))
    print(tmp[0]+tmp[1])


##BOJ 11021
n = int(input())
for i in range(n):
    tmp = list(map(int, input().split()))
    result = tmp[0]+ tmp[1]
    answer = 'Case #{}: {}'.format(i+1,result)
    print(answer)

##BOJ 11718
while True:
    try :
        print(input())
    except EOFError:
        break