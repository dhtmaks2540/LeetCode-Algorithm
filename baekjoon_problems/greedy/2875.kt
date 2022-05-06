import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.min

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    var (n, m, k) = br.readLine().split(" ").map { it.toInt() }

    for(i in 0 until k) {
        if(n / 2 > m) n--
        else m--
    }

    print(min(n, m))
}