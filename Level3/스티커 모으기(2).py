def solution(sticker):
    answer = 36
    len_sticker = len(sticker)
    if len_sticker == 1:
        return sticker[0]
    dp1 = [0] * len_sticker
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    ## 처음 스티커를 땔경우
    ## dp[1]부터 사용하지 않을 경우 사용해서 다음 꺼를 사용할 경우 중 큰 경우를 고른다.
    for i in range(2, len_sticker - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])

    tmp_value1 = max(dp1)

    ## 처음 스티커를 때지 않을 경우
    dp2 = [0] * len_sticker
    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2, len_sticker):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    tmp_value2 = max(dp2)
    return max(tmp_value1, tmp_value2)