def solution(users, emoticons):
    # 이모티콘 플러스 서비스 가입자 최대한 늘리기 -> 판매액 늘리기
    # n명의 카톡 사용자들에게 이모티콘 m개 할인하여 판매
    # 자신의 기준에 따라 일정비율 이상 모두 구매
    # 이모티콘 구매 비용이 일정 가격 이상 -> 구매 모두 취소후 임티 플러스
    # 행사 목적을 최대한으로 달성했을 때 이모티콘 플러스 서비스 가입 수와 이모티콘 매출액
    ## 비율 -> 10, 20, 30, 40
    n = len(emoticons)
    global res
    res = []
    def dfs(depth, rates):
        global res
        if depth == n:
            cnt, price_sum = 0, 0
            for u_rate, u_money in users:
                temp, check = 0, False
                for i in range(len(emoticons)):
                    if u_rate <= rates[i]:
                        temp += emoticons[i] - emoticons[i] * (rates[i] / 100)
                    if temp >= u_money:
                        cnt += 1
                        check = True
                        break
                if not check:
                    price_sum += temp
            res.append([cnt, int(price_sum)])
            return

        dfs(depth+1, rates + [40])
        dfs(depth+1, rates + [30])
        dfs(depth+1, rates + [20])
        dfs(depth+1, rates + [10])
    dfs(0, [])
    res.sort(key=lambda x:(x[0], x[1]), reverse=True)
    return res[0]