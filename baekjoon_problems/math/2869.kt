import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (A, B, V) = readLine().split(" ").map { it.toInt() }

    val day = (V - B) / (A - B)
    if((V - B) % (A - B) != 0) println(day + 1)
    else println(day)
}