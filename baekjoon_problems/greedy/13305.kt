import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val roadArray = LongArray(n - 1)
    val priceArray = LongArray(n)

    var st = StringTokenizer(readLine(), " ")
    repeat(n - 1) { index ->
        roadArray[index] = st.nextToken().toLong()
    }

    st = StringTokenizer(readLine(), " ")
    repeat(n) { index ->
        priceArray[index] = st.nextToken().toLong()
    }

    var price: Long = 0
    var index = 0
    var nowIndex = 0

    while(index <= n - 2) {
        nowIndex = index

        price += priceArray[nowIndex] * roadArray[index]
        index++

        if(priceArray[nowIndex] <= priceArray[index]) {
            while(index <= n - 2 && priceArray[nowIndex] <= priceArray[index]) {
                price += priceArray[nowIndex] * roadArray[index]
                index++
            }
        }
    }

    println(price)
}