package programmers

class Solution {
    var plus = 0
    var price = 0
    val salePercent = intArrayOf(10, 20, 30, 40)

    fun solution(users: Array<IntArray>, emoticons: IntArray): IntArray {
        permutation(0, users, emoticons, intArrayOf())
        return intArrayOf(plus, price)
    }

    fun permutation(depth: Int, users: Array<IntArray>, emoticons: IntArray, percents: IntArray) {
        if (depth == emoticons.size) {
            var salePlus = 0
            var sum = 0

            users.forEach { userInfo ->
                var pay = 0

                val wantPercent = userInfo[0]
                val maxPrice = userInfo[1]

                percents.forEachIndexed { index, percent ->
                    if (percent >= wantPercent) {
                        pay += getSalePrice(percent, emoticons[index])
                    }
                }

                if (maxPrice <= pay) salePlus++
                else sum += pay
            }

            if (plus < salePlus) {
                plus = salePlus
                price = sum
            } else if (plus == salePlus) {
                price = maxOf(price, sum)
            }

            return
        }

        for (percent in salePercent) {
            permutation(depth + 1, users, emoticons, percents + percent)
        }
    }

    fun getSalePrice(salePercent: Int, price: Int): Int =
        price * (100 - salePercent) / 100
}
