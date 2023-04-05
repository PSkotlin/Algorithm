import sys
from itertools import combinations
inp = lambda : sys.stdin.readline().split()
N, M = map(int, inp())
# 치킨 거리 : 집과 가장 가까운 치킨집 사이의 거리 -> 이 치킨 거리들의 합
# 치킨집 중에서 최대 M개 고르고 나머지 폐업
# | r1-r2 | + | c1 - c2|
# 1은 집, 2는 치킨집
dx = [0, 0, 1, -1]
dy = [1, -1 ,0, 0]
city = []
stores, homes = [], []
for i in range(N):
    temp = list(map(int, inp()))
    for j in range(N):
        if temp[j] == 2:
            stores.append((i, j))
        elif temp[j] == 1:
            homes.append((i, j))
    city.append(temp)
# 치킨 집을 하나 씩 폐업 해보기

# distances[i][j] -> i번째 집에서 j번째 치킨집까지 거리
len_s, len_h = len(stores), len(homes)
distances = [[0 for _ in range(len_s)] for _ in range(len_h)]
for i in range(len_h):
    for j in range(len_s):
        distances[i][j] = abs(homes[i][0] - stores[j][0]) + abs(homes[i][1] - stores[j][1])

res = sys.maxsize
def backtrack(store_can):
    global res
    # 치킨 거리 구하기
    distance = 0

    for i in range(len(homes)):
        min_temp = sys.maxsize
        for j in range(len(stores)):
            if store_can[j]:
                min_temp = min(min_temp, distances[i][j])
        distance += min_temp

    if res > distance:
        res = distance
    return

# stores 배열 중 M개를 뽑아 backtrack 함수에 넣기
store_avail = [False for _ in range(len_s)]
index_list = [i for i in range(len_s)]
for store_comb in combinations(index_list, M):
    store_list = list(store_comb)
    for s in store_list:
        store_avail[s] = True
    backtrack(store_avail)
    for s in store_list:
        store_avail[s] = False
print(res)