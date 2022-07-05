import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val queue = PriorityQueue<Int>()
    val sb = StringBuilder()

    repeat(n) { _ ->
        val x = readLine().toInt()
        if(x == 0) {
            if(queue.isEmpty())
                sb.append("0\n")
            else
                sb.append("${-queue.poll()}\n")
        } else
            queue.add(-x)
    }

    println(sb.toString())
}