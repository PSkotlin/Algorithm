package programmers

class Solution {

    fun solution(s: String): Int {
        var answer = s.length

        for (limit in 1 until s.length) {
            val sb = StringBuilder()
            var now = s.substring(0 until limit)
            var repeat = 1

            for (j in limit until s.length step limit) {
                val start = j
                val end = minOf(j + limit, s.length)
                val next = s.substring(start until end)

                if (now == next) {
                    repeat++
                } else {
                    if (repeat > 1) sb.append(repeat)
                    sb.append(now)
                    now = next
                    repeat = 1
                }
            }

            if (repeat > 1) sb.append(repeat)
            sb.append(now)
            answer = minOf(sb.length, answer)
        }

        return answer
    }
}

fun main() {
    println(Solution().solution("abcabcabcabcdededededede"))
}