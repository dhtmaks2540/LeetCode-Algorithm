import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    var cnt = 1
    var num = 666

    while(cnt != n) {
        num++

        if(num.toString().contains("666")) cnt++
    }

    println(num)
}