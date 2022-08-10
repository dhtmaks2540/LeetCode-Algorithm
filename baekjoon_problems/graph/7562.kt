import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val t = readLine().toInt()
    val dxy = arrayOf(Pair(-1, -2), Pair(-2, -1), Pair(1, -2), Pair(2, -1),
            Pair(-1, 2), Pair(-2, 1), Pair(1, 2), Pair(2, 1))
    val sb = StringBuilder()

    repeat(t) { _ ->
        val l = readLine().toInt()
        var st = StringTokenizer(readLine(), " ")
        var nowRow = st.nextToken().toInt()
        var nowCol = st.nextToken().toInt()

        st = StringTokenizer(readLine(), " ")
        val toRow = st.nextToken().toInt()
        val toCol = st.nextToken().toInt()

        val visited = Array(l) { BooleanArray(l) }
        val queue = ArrayDeque<Pair<Int, Int>>()
        queue.add(Pair(nowRow, nowCol))
        visited[nowRow][nowCol] = true
        var answer = -1
        var check = false

        while(queue.isNotEmpty()) {
            answer++
            for(i in queue.indices) {
                val pair = queue.pollFirst()
                nowRow = pair.first
                nowCol = pair.second

                if(nowRow == toRow && nowCol == toCol) {
                    check = true
                    break
                }

                for(index in dxy.indices) {
                    val nextRow = nowRow + dxy[index].first
                    val nextCol = nowCol + dxy[index].second

                    if(nextRow in 0 until l && nextCol in 0 until l && !visited[nextRow][nextCol]) {
                        visited[nextRow][nextCol] = true
                        queue.add(Pair(nextRow, nextCol))
                    }
                }
            }

            if(check) {
                sb.append("$answer\n")
                break
            }
        }
    }

    println(sb.toString())
}