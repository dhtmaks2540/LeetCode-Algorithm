import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val map = hashMapOf(
        ')' to '(',
        ']' to '['
    )

    val sb = StringBuilder()

    while(true) {
        val lines = readLine().toCharArray()

        if(lines[0] == '.')
            break

        val stack = Stack<Char>()
        var balanceCheck = true

        for(chr in lines) {
            if(chr in "([")
                stack.add(chr)
            else if(chr in ")]") {
                if(stack.isNotEmpty() && stack.lastElement() == map[chr])
                    stack.pop()
                else {
                    balanceCheck = false
                    break
                }
            }
        }

        if(!balanceCheck || stack.isNotEmpty())
            sb.append("no\n")
        else
            sb.append("yes\n")
    }

    println(sb.toString())
}