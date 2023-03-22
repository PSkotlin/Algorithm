import sys
inp = lambda : sys.stdin.readline()
for _ in range(int(inp())):
    n = int(inp())
    up_sticker = list(map(int, inp().split()))
    down_sticker = list(map(int, inp().split()))
    # 위의 스티커를 사용하는 경우, 아래 스티커를 사용하는 경우
    max_up, max_down = 0, 0
    for i in range(n):
        max_up, max_down = max(max_up, max_down + up_sticker[i]), max(max_down, max_up + down_sticker[i])
    print(max(max_up, max_down))
    # scores = [list(map(int, inp().split())) for _ in range(2)]
    # dp = [[0 for _ in range(n+1)] for _ in range(2)]
    # for j in range(1, n+1):
    #     for i in range(2):
    #         # 이 스티커틀 사용하는 경우 + 사용하지 않는 경우
    #         dp[i][j] = max(dp[1-i][j-1] + scores[i][j-1], dp[i][j-1])
    # print(max(dp[0][-1], dp[1][-1]))