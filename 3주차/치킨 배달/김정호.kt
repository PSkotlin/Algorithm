import kotlin.math.abs

lateinit var array: Array<IntArray>
val chickens = ArrayList<Pair<Int, Int>>()
val homes = ArrayList<Pair<Int, Int>>()
lateinit var visited: BooleanArray
var answer = Int.MAX_VALUE

fun main() = with(System.`in`.bufferedReader()) {
    val (n, m) = readLine().split(" ").map { it.toInt() }

    array = Array(n) { IntArray(n) }

    repeat(n) {
        array[it] = readLine().split(" ").map { it.toInt() }.toIntArray()
    }

    repeat(n) { i ->
        repeat(n) { j ->
            when (array[i][j]) {
                1 -> homes.add(i to j)
                2 -> chickens.add(i to j)
            }
        }
    }

    visited = BooleanArray(chickens.size)
    backTracking(0, 0, m)
    println(answer)
}

fun backTracking(index: Int, count: Int, max: Int) {
    if (count == max) {
        answer = minOf(answer, getDiff())
        return
    }

    for (i in index until chickens.size) {
        if (!visited[i]) {
            visited[i] = true
            backTracking(i, count + 1, max)
            visited[i] = false
        }
    }
}

fun getDiff(): Int {
    var shortDistance = 0

    homes.forEach { home ->
        var d = Int.MAX_VALUE

        chickens.forEachIndexed { index, value ->
            if (visited[index]) {
                val x = abs(value.first - home.first)
                val y = abs(value.second - home.second)

                d = minOf(x + y, d)
            }
        }

        shortDistance += d
    }

    return shortDistance
}

