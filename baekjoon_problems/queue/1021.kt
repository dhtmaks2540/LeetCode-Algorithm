import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var st = StringTokenizer(readLine(), " ")
    val n = st.nextToken().toInt()
    val m = st.nextToken().toInt()

    val targetArray = IntArray(m)
    st = StringTokenizer(readLine(), " ")
    repeat(m) { index ->
        targetArray[index] = st.nextToken().toInt()
    }

    val queue = ArrayDeque<Int>(n)
    for(i in 1..n) {
        queue.add(i)
    }

    var opeCnt = 0
    var index = 0

    while(index < m) {
        val targetIndex = queue.indexOf(targetArray[index])

        if(targetIndex <= queue.size / 2) {
            while(queue.peekFirst() != targetArray[index]) {
                queue.add(queue.pollFirst())
                opeCnt++
            }
        } else {
            while(queue.peekFirst() != targetArray[index]) {
                queue.addFirst(queue.pollLast())
                opeCnt++
            }
        }

        queue.pollFirst()
        index++
    }

    println(opeCnt)
}