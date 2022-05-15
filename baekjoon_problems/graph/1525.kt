import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val graph = Array<Array<Int>>(3) { Array(3) { 0 } }
    for(i in 0 until 3) {
        val st = StringTokenizer(br.readLine(), " ")
        for(j in 0 until 3) {
            graph[i][j] = st.nextToken().toInt()
        }
    }

    val moveDir = listOf<Pair<Int, Int>>(Pair(0, 1), Pair(0, -1), Pair(1, 0), Pair(-1, 0))
    val target = 123456789

    var start = 0
    for(i in 0 until 3) {
        for(j in 0 until 3) {
            if(graph[i][j] == 0)
                graph[i][j] = 9
            start = start * 10 + graph[i][j]
        }
    }

    fun toInt(lis: List<Char>): Int {
        var ret = 0
        for(x in lis) {
            ret = ret * 10 + Character.getNumericValue(x)
        }

        return ret
    }

    val queue = ArrayDeque<Int>()
    queue.add(start)
    val visited = mutableMapOf<Int, Int>()
    visited[start] = 0

    while(queue.isNotEmpty()) {
        val cur = queue.pollFirst()
        val strCur = cur.toString()

        if(cur == target) break

        val zeroIndex = strCur.indexOf('9')
        val yIndex = zeroIndex / 3
        val xIndex = zeroIndex % 3

        for(i in 0 until 4) {
            val nextY = yIndex + moveDir[i].first
            val nextX = xIndex + moveDir[i].second

            if(nextX in 0..2 && nextY in 0..2) {
                val temp = strCur.toMutableList()
                val tempValue = temp[yIndex * 3 + xIndex]
                temp[yIndex * 3 + xIndex] = temp[nextY * 3 + nextX]
                temp[nextY * 3 + nextX] = tempValue

                val nextCur = toInt(temp)

                if(!visited.containsKey(nextCur)) {
                    visited[nextCur] = visited[cur]?.plus(1)!!
                    queue.add(nextCur)
                }
            }
        }
    }

    if(!visited.containsKey(target)) print(-1)
    else print(visited[target])
}