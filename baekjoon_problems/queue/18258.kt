import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val queue = ArrayDeque<String>()
    val sb = StringBuilder()

    repeat(n) { _ ->
        val nowOrder = readLine().split(" ")
        if(nowOrder[0] == "push") {
            queue.add(nowOrder[1])
        } else if(nowOrder[0] == "front") {
            if(queue.isEmpty())
                sb.append("-1\n")
            else
                sb.append("${queue.peekFirst()}\n")
        } else if(nowOrder[0] == "back") {
            if(queue.isEmpty())
                sb.append("-1\n")
            else
                sb.append("${queue.peekLast()}\n")
        } else if(nowOrder[0] == "empty") {
            if(queue.isEmpty())
                sb.append("1\n")
            else
                sb.append("0\n")
        } else if(nowOrder[0] == "pop") {
            if(queue.isEmpty())
                sb.append("-1\n")
            else
                sb.append("${queue.pollFirst()}\n")
        } else if(nowOrder[0] == "size")
            sb.append("${queue.size}\n")
    }

    println(sb.toString())
}