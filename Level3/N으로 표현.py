def solution(N, number):
    answer = -1
    DP = []

    for i in range(1, 9):
        nset = { int(str(N) * i) }

        for j in range(0, i - 1):
            for x in DP[j]:
                for y in DP[-j - 1]:
                    nset.add(x + y)
                    nset.add(x - y)
                    nset.add(x * y)

                    if y != 0:
                        nset.add(x // y)

        if number in nset:
            return i

        DP.append(nset)

    return answer