import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val k = readLine().toInt()
    val stack = Stack<Int>()

    repeat(k) { _ ->
        val num = readLine().toInt()
        if(num == 0)
            stack.pop()
        else
            stack.add(num)
    }

    println(stack.sum())
}