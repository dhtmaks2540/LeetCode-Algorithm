import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val st = StringTokenizer(readLine(), " ")
    val a = st.nextToken().toLong()
    val b = st.nextToken().toLong()
    val c = st.nextToken().toLong()

    fun pow(exponent: Long): Long {
        if(exponent == 1L)
            return a % c

        val temp = pow(exponent / 2)

        if(exponent % 2 == 1L)
            return (temp * temp % c) * a % c

        return temp * temp % c
    }

    println(pow(b))
}