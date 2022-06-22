import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.ArrayDeque

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val t = readLine().toInt()
    val sb = StringBuilder()
    repeat(t) { _ ->
        val funcArray = readLine().toCharArray()
        val n = readLine().toInt()
        var numStr = readLine()
        numStr = numStr.slice(1 until numStr.length - 1).trim()
        val numArray = numStr.split(",")
        val queue = ArrayDeque<String>()

        for(num in numArray) {
            try {
                num.toInt()
                queue.add(num)
            } catch (e: Exception) {
                continue
            }
        }

        var errorCheck = false
        var reverseCheck = false

        for(func in funcArray) {
            if(func == 'R')
                reverseCheck = !reverseCheck
            else {
                if(queue.isEmpty()) {
                    errorCheck = true
                    break
                } else {
                    if (reverseCheck)
                        queue.pollLast()
                    else
                        queue.pollFirst()
                }
            }
        }

        when {
            errorCheck -> sb.append("error\n")
            queue.isEmpty() -> sb.append("[]\n")
            else -> {
                if(reverseCheck) {
                    val newList = queue.reversed()
                    sb.append(newList.joinToString(separator = ",", prefix = "[", postfix = "]") + "\n")
                } else {
                    sb.append(queue.joinToString(separator = ",", prefix = "[", postfix = "]") + "\n")
                }
            }
        }
    }

    println(sb.toString())
}