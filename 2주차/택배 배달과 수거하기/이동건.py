from collections import deque
def solution(cap, n, deliveries, pickups):
    # 배달할 택배 상자 실어 물류창고에서 출발하면서 배달, 빈 택배 상자 수거
    # 배달 + 수거 -> cap개
    # delivers 기준으로 물류창고를 다녀와야함
    deliver_q, pickup_q = deque(), deque()
    box = [0, 0]
    d_idx, p_idx = n-1, n-1
    while d_idx > -1:
        # index를 큐에다가 추가
        # 몇 개가 있는지에 대한 정보 알아야함
        if not box[0] and deliveries[d_idx]:
            deliver_q.append(d_idx + 1)
        check = box[0] + deliveries[d_idx] - cap
        # 현재 deliveries에 있는 값을 넣으면 cap 초과
        if check > 0:
            deliveries[d_idx] -= cap - box[0]
            box[0] = 0
        else:
            box[0] += deliveries[d_idx]
            deliveries[d_idx] = 0
            if not d_idx: break
            d_idx -= 1

    while p_idx > - 1:
        if not box[1] and pickups[p_idx]:
            pickup_q.append(p_idx + 1)
        check = box[1] + pickups[p_idx] - cap
        if check > 0:
            pickups[p_idx] -= cap - box[1]
            box[1] = 0
            continue
        else:
            box[1] += pickups[p_idx]
            pickups[p_idx] = 0
            if not p_idx: break
        p_idx -= 1
    res = 0
    for _ in range(min(len(deliver_q), len(pickup_q))):
        temp_d, temp_p = deliver_q.popleft(), pickup_q.popleft()
        res += max(temp_d, temp_p)
    while deliver_q:
        res += deliver_q.popleft()
    while pickup_q:
        res += pickup_q.popleft()
    return res * 2

def solution2(cap, n, deliveries, pickups):
    idx = n - 1
    total_distance = 0

    while idx >= 0:
        d_sum, p_sum = 0, 0

        while idx >= 0 and not deliveries[idx] and not pickups[idx]:
            idx -= 1

        distance = (idx + 1) * 2
        total_distance += distance

        while idx >= 0 and d_sum + deliveries[idx] <= cap and p_sum + pickups[idx] <= cap:
            d_sum += deliveries[idx]
            p_sum += pickups[idx]
            idx -= 1

        deliveries[idx] -= (cap - d_sum)
        pickups[idx] -= (cap - p_sum)

    return total_distance