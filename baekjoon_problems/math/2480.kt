import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (a, b, c) = readLine().split(" ").map { it.toInt() }

    if(a == b && b == c) println(10000 + a * 1000)
    else if(a == b || b == c || c == a) {
        when {
            a == b -> print(1000 + a * 100)
            b == c -> print(1000 + b * 100)
            else -> print(1000 + c * 100)
        }
    }
    else print(arrayOf(a, b, c).maxOrNull()?.times(100))
}