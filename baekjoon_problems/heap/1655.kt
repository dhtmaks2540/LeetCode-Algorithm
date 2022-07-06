import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val minPq = PriorityQueue<Int>()
    val maxPq = PriorityQueue<Int>()
    val sb = StringBuilder()

    repeat(n) { _ ->
        val value = readLine().toInt()

        if(maxPq.size > minPq.size)
            minPq.add(value)
        else
            maxPq.add(-value)

        if(minPq.isNotEmpty() && maxPq.isNotEmpty()) {
            if(-maxPq.peek() > minPq.peek()) {
                val maxValue = -maxPq.poll()
                val minValue = minPq.poll()

                maxPq.add(-minValue)
                minPq.add(maxValue)
            }
        }

        sb.append("${-maxPq.peek()}\n")
    }

    println(sb.toString())
}