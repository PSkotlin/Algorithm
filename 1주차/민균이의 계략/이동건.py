import sys, bisect
inp = lambda : sys.stdin.readline()
N = int(inp())
# 증가하는 수열이면서 개수가 최대여야 함 => 가장 긴 증가하는 수열
cards = list(map(int, inp().split()))
lis = [1 for _ in range(N)]
# 현재 위치 보다 이전에 있는 원소가 작은지 확인 -> 작다면 현재 위치 이전 숫자 중 dp 최댓값 구하기 + 1
## 6
## 8 9 1 2 3 10
# 증가하는 부분 수열에 대한 것을 저장해두면 더 빠르게 처리 가능
dp = [cards[0]]
# 오름차순 으로 dp 배열 설계 -> binary search 사용됨
for i in range(N):
    if dp[-1] < cards[i]:
        dp.append(cards[i])
    else:
        idx = bisect.bisect_left(dp, cards[i])
print(len(dp))
# for i in range(N):
#     for j in range(i):
#         if cards[i] > cards[j]:
#             lis[i] = max(lis[i], lis[j]+1)
# print(max(lis))