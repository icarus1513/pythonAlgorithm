
def solution():
   n = int(input())
   array = list(map(int,input().split()))

   # 결과 저장하기 위한 DP
   dp = [0] * 2

   dp[0] = array[0]
   dp[1] = max(array[0], array[1])
   for i in range(2,n):
       dp.append(max(dp[i-1], dp[i-2] + array[i]))

   print(dp)
   return None

if __name__ == "__main__":
    solution()

# input case
# 4
# 1 3 1 5