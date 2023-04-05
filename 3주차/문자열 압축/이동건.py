def solution(s):
    # 문자열은 제일 앞 부터 정해진 길이 단위로 잘라야 함
    # 문자 자르는 단위 1개부터 체크
    # 문자를 몇 개 단위로 자를 건지가 관건
    n = len(s)
    def answer(size):
        temp_res = ""
        i = 0
        while i + size < n:
            temp = s[i:i+size]
            j = i
            cnt = 0
            while j < n and s[j:j+size] == temp:
                cnt += 1
                j += size
            if cnt == 1:
                temp_res += temp
            else:
                temp_res += str(cnt) + temp
            i = j
        # 문자 남은 경우
        if i < n and i + size >= n:
            temp_res += s[i:]
        return len(temp_res)
    res = n
    for i in range(1, n // 2 + 1):
        res = min(res, answer(i))
    return res

def solution2(s):
    n = len(s)
    res = n
    for k in range(1, n // 2 + 1):
        temp_res = ''
        prev, temp = '', ''
        cnt = 1
        for i in range(0, n, k):
            temp = s[i:i+k]
            if prev == temp:
                cnt += 1
            else:
                if cnt > 1:
                    temp_res += str(cnt) + prev
                    cnt = 1
                else:
                    temp_res += prev
                prev = temp
        # for문 후 cnt 값이 1보다 크다 -> 문자열 연속했지만 아직 안붙임
        if cnt > 1:
            temp_res += str(cnt) + prev
        # cnt 값이 1 -> 마지막에서 else문 발동 -> temp값 붙이기
        else:
            temp_res += temp

        res = min(res, len(temp_res))
    return res
print(solution2("abcabcdede"))