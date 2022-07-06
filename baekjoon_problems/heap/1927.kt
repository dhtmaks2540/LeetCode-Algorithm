import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val sb = StringBuilder()
    val pq = PriorityQueue<Int>()

    repeat(n) { _ ->
        val x = readLine().toInt()
        if(x == 0) {
            if(pq.isEmpty())
                sb.append("0\n")
            else
                sb.append("${pq.poll()}\n")
        }
        else
            pq.add(x)
    }

    println(sb.toString())
}