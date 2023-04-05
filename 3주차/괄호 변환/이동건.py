def solution(p):
    # int_p = []
    # for c in list(p):
    #     if c == '(':
    #         int_p.append(0)
    #     else:
    #         int_p.append(1)

    # 빈 문자열이면 빈 문자열 반환
    # '(' 와 ')'의 개수가 같으면 균형잡힌 괄호 문자열
    # 문자열 w -> u, v로 분리 / u는 균형잡인 괄호 문자열로 더 이상 분리 x, v 빈 문자열 가능
    # u가 올바른 문자열 -> v에 대해 1단계부터 -> u에 붙이기

    # u가 올바른 문자열 x
    ## 빈 문자열에 (
    ## 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 이어 붙이기
    ## ) 다시 붙이기
    ## u의 첫 번째와 마지막 문자 제거, 나머지 문자열의 괄호 방향 뒤집기
    def iterative(w):
        if not w:
            return []

        cnt_0, cnt_1 = 0, 0
        check = True
        u, v = [], []
        for i in range(len(w)):
            if w[i] == '(':
                cnt_0 += 1
            else:
                cnt_1 += 1

            if cnt_1 > cnt_0:
                check = False

            if cnt_0 and cnt_0 == cnt_1:
                u, v = w[:i + 1], w[i + 1:]
                break

        if check:
            return u + iterative(v)

        else:
            temp_v = ['('] + iterative(v) + [')']
            temp_u = u[1:-1]

            for i in range(len(temp_u)):
                if temp_u[i] == '(':
                    temp_u[i] = ')'
                else:
                    temp_u[i] = '('
            return temp_v + temp_u

    # res = ''
    # for i in iterative(int_p):
    #     if not i:
    #         res += '('
    #     else:
    #         res += ')'
    return ''.join(iterative(list(p)))