import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val array = IntArray(n)
    val st = StringTokenizer(readLine(), " ")
    repeat(n) { index ->
        array[index] = st.nextToken().toInt()
    }
    val stack = Stack<Int>()

    for (i in 0 until n) {
        while (stack.isNotEmpty() && array[stack.peek()] < array[i]) {
            array[stack.pop()] = array[i]
        }
        stack.push(i)
    }

    while (stack.isNotEmpty()) {
        array[stack.pop()] = -1
    }

    val sb = StringBuilder()
    array.forEach { sb.append("$it ") }
    println(sb.toString())
}