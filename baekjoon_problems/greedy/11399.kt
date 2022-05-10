import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    val array = Array<Int> (n) { 0 }
    val st = StringTokenizer(br.readLine(), " ")
    for(i in 0 until n) {
        array[i] = st.nextToken().toInt()
    }

    array.sort()

    var sumTime = 0
    var answer = 0

    for(time in array) {
        sumTime += time
        answer += sumTime
    }

    print(answer)
}