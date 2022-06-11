import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val price = Array(n){ IntArray(3) }
    repeat(n) { row ->
        val st = StringTokenizer(readLine(), " ")
        repeat(3) { col ->
            price[row][col] = st.nextToken().toInt()
        }
    }

    for(i in 1 until n) {
        for(j in 0 until 3) {
            var minPrice = Int.MAX_VALUE
            for(k in 0 until 3) {
                if(j != k && minPrice > price[i - 1][k])
                    minPrice = price[i - 1][k]
            }
            price[i][j] += minPrice
        }
    }

    println(price[n - 1].minOrNull())
}