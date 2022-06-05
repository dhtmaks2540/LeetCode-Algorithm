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

    if(n == 1) {
        println(array[0] * array[0])
    } else {
        array.sort()
        println(array[0] * array[array.lastIndex])
    }
}