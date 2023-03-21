fun main() = with(System.`in`.bufferedReader()) {
    val (N, M) = readLine().split(" ").map { it.toInt() }
    val sb = StringBuilder()

    val listeners = HashSet<String>()
    val answers = ArrayList<String>()

    repeat(N) { listeners.add(readLine()) }
    repeat(M) {
        readLine().apply {
            if(listeners.contains(this)) answers.add(this)
        }
    }

    sb.appendLine(answers.size)
    answers.sorted().forEach { sb.appendLine(it) }

    println(sb)
}
