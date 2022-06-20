import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.ArrayDeque

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val queue = ArrayDeque<Int>()

    for(i in 1..n) {
        queue.add(i)
    }

    while(queue.size != 1) {
        queue.pollFirst()
        queue.add(queue.pollFirst())
    }

    println(queue.pollFirst())
}