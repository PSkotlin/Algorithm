package programmers

class Solution {
    fun solution(cap: Int, n: Int, deliveries: IntArray, pickups: IntArray): Long {
        var deliver = 0
        var pickup = 0
        var answer = 0L

        for (i in n - 1 downTo 0) {
            if (deliveries[i] != 0 || pickups[i] != 0) {
                var cnt = 0

                while (deliver < deliveries[i] || pickup < pickups[i]) {
                    cnt++
                    deliver += cap
                    pickup += cap
                }

                deliver -= deliveries[i]
                pickup -= pickups[i]
                answer += ((i + 1) * cnt * 2).toLong()
            }
        }

        return answer
    }
}
