import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Integer.min

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))

    val (N, M) = br.readLine().split(" ").map { it.toInt() }

    when {
        N == 1 -> {
            println(1)
        }
        N == 2 -> {
            println(min(4, (M + 1) / 2))
        }
        M < 7 -> {
            println(min(4, M))
        }
        else -> {
            print(M - 7 + 5)
        }
    }
}