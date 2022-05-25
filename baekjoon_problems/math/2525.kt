import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (nowHour, nowMin) = readLine().split(" ").map { it.toInt() }
    var needMin = readLine().toInt()

    val needHour = needMin / 60
    needMin %= 60

    var resultHour = nowHour + needHour
    var resultMin = nowMin + needMin

    if(resultMin >= 60) {
        resultMin -= 60
        resultHour++
    }

    if(resultHour >= 24) {
        resultHour -= 24
    }

    println("$resultHour $resultMin")
}