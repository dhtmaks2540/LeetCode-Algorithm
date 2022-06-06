import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val array = readLine().split(" ").map { it.toInt() }

    for(i in 1 until n) {
        for(j in array[i] downTo 0) {
            if(array[0] % j == 0 && array[i] % j == 0) {
                println("${array[0] / j}/${array[i] / j}")
                break
            }
        }
    }
}