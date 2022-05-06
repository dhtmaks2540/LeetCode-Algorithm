import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    var (n, k) = br.readLine().split(" ").map { it.toInt() }
    val array = Array<Int> (n) { 0 }
    for(i in 0 until n) {
        array[i] = br.readLine().toInt()
    }
    // 거꾸로 뒤집기(내림차순)
    array.reverse()
    var answer = 0

    for(coin in array) {
        answer += k / coin
        k %= coin
    }

    print(answer)
}