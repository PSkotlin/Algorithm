package programmers

import java.util.*

class Solution {
    fun solution(w: String): String {
        val sb = StringBuilder()

        // 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
        if (w.isBlank()) return ""

        // 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
        var left = 0
        var right = 0
        var index = 0
        for (i in w.indices) {
            if (w[i] == '(') left++
            else if (w[i] == ')') right++

            if (left == right) {
                index = i
                break
            }
        }

        var u = w.substring(0..index)
        var v = w.substring(index + 1..w.lastIndex)

        // 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
        if (check(u)) {
            u += solution(v)
            // 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
            sb.append(u)
        } else {
            // 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
            sb.append("(") //   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
            sb.append(solution(v)) //   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
            sb.append(")") //   4-3. ')'를 다시 붙입니다.

            // 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
            u.drop(0)
            u.dropLast(0)

            u = u.substring(1 until u.lastIndex)

            for (i in u.indices) {
                if (u[i] == '(') sb.append(")")
                else sb.append("(")
            }
        }

        // 4-5. 생성된 문자열을 반환합니다.
        return sb.toString()
    }

    fun check(p: String): Boolean {
        val stack = Stack<Char>()

        p.forEach {
            if (it == '(') stack.push(it)
            else {
                if (stack.isNotEmpty()) {
                    stack.pop()
                }
            }
        }

        return stack.isEmpty()
    }
}