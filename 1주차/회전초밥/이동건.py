import sys
inp = lambda : sys.stdin.readline()
# k개 접시 연속해서 먹으면 할인된 가격
# 초밥의 종류가 하나 쓰인 쿠폰 -> 쿠폰에 적혀진 초밥 하나로 무료 제공
N, d, k, c = map(int, inp().split())
sushi = [int(inp()) for _ in range(N)]
# 초밥 번호를 인자로 가지는 리스트 만들기
select = [0] * (d+1)
cnt = 0
for num in sushi[:k]:
    if not select[num]:
        cnt += 1
    select[num] += 1
res = cnt
# k번째 까지 c 없었음 하나 추가
if not select[c]:
    res += 1

for i in range(N):
    # 없애려는 초밥이 한 개 남은 경우
    if select[sushi[i]] == 1:
        cnt -= 1
    select[sushi[i]] -= 1

    # 새로 추가 하려는 초밥이 원래 없는 경우
    if not select[sushi[(i+k) % N]]:
        cnt += 1
    select[sushi[(i+k) % N]] += 1

    if res <= cnt:
        res = cnt
        # 없앤 것이 쿠폰 초밥인 경우 => 최대
        if not select[c]:
            res += 1
print(res)

## 연속해서 k개, 쿠폰 번호 c

# sushi_counter = Counter(sushi[:k])
# sushi_counter[c] += 1
# res = 1
# for i in range(N):
#     if sushi_counter[sushi[i]] == 1:
#         del sushi_counter[sushi[i]]
#     else:
#         sushi_counter[sushi[i]] -= 1
#     sushi_counter[sushi[(i+k) % N]] += 1
#     res = max(res, len(sushi_counter))
# print(res)