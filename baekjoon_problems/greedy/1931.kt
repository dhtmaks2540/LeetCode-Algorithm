import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    val array = Array<Array<Int>>(n) { Array(2) { 0 } }

    for(i in 0 until n) {
        val (start, end) = br.readLine().split(" ").map { it.toInt() }
        array[i][0] = start
        array[i][1] = end
    }
    
    array.sortWith(compareBy({it[1]}, {it[0]}))

    var time = 0
    var answer = 0

    for((start, end) in array) {
        if(time <= start) {
            time = end
            answer += 1
        }
    }

    println(answer)
}