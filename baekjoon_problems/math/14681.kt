import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val x = readLine().toInt()
    val y = readLine().toInt()

    if(x > 0) {
        if(y > 0) println(1)
        else println(4)
    } else {
        if(y > 0) println(2)
        else println(3)
    }
}