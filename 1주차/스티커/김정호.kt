import kotlin.math.max

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()

    repeat(n) {
        val size = readLine().toInt()
        val stickers = Array(2) { IntArray(size) }

        repeat(2) {
            stickers[it] = readLine().split(" ").map { it.toInt() }.toIntArray()
        }

        val dp = Array(2) { IntArray(size) }.apply {
            this[0][0] = stickers[0][0]
            this[1][0] = stickers[1][0]

            if(size >= 2) {
                this[0][1] = stickers[0][1] + stickers[1][0]
                this[1][1] = stickers[0][0] + stickers[1][1]
            }
        }

        for (i in 2 until size) {
            for (j in 0 until 2) {
                dp[j][i] = maxOf(dp[(j + 1) % 2][i - 1], dp[(j + 1) % 2][i - 2]) + stickers[j][i]
            }
        }

        println(max(dp[0].last(), dp[1].last()))
    }
}
