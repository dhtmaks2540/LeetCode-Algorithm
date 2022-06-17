import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val correctArray = IntArray(n)
    repeat(n) { index ->
        correctArray[index] = readLine().toInt()
    }

    val stack = Stack<Int>()
    val array = IntArray(n) { i -> i + 1 }
    var index = 0
    val sb = StringBuilder()

    array.forEach { num ->
        stack.add(num)
        sb.append("+\n")

        if(stack.lastElement() == correctArray[index]) {
            while (index < n && stack.isNotEmpty() && stack.lastElement() == correctArray[index]) {
                stack.pop()
                sb.append("-\n")
                index++
            }
        }
    }

    if(stack.isEmpty()) {
        println(sb.toString())
    } else {
        println("NO")
    }
}