import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.sqrt

private const val MAX_VALUE = 10000

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val primeNum = Array(MAX_VALUE + 1) { true }

    for(i in 2..sqrt(MAX_VALUE.toDouble()).toInt()) {
        if(primeNum[i]) {
            var j = 2
            while(i * j <= MAX_VALUE) {
                primeNum[i * j] = false
                j++
            }
        }
    }

    val t = readLine().toInt()

    for(i in 0 until t) {
        val target = readLine().toInt()

        for(j in target / 2 downTo 2) {
            if(primeNum[j] && primeNum[target - j]) {
                println("$j ${target - j}")
                break
            }
        }
    }
}