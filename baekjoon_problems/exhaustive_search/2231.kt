import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.system.exitProcess

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()

    for(num in 1 until n) {
        var sumValue = num
        for(chr in num.toString()) {
            sumValue += chr.toString().toInt()
        }

        if(sumValue == n) {
            println(num)
            exitProcess(0)
        }
    }

    println(0)
}