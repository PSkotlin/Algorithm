fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val numbers = readLine().split(" ").map { it.toInt() }.toIntArray()
    val dp = ArrayList<Int>()

    dp.add(numbers[0])

    for (i in 1 until numbers.size) {
        val index = lowerBound(0, dp.size, numbers[i], dp)

        if(dp.size <= index) dp.add(numbers[i])
        else dp[index] = numbers[i]
    }

    println(dp.size)
}

fun lowerBound(start: Int, end: Int, target: Int, dp: ArrayList<Int>): Int {
    var left = start
    var right = end

    while (left < right) {
        val middle = (left + right) / 2

        if (dp[middle] < target) left = middle + 1
        else right = middle
    }

    return right
}
