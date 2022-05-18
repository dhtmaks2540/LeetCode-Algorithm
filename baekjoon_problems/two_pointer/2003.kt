import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (N, M) = br.readLine().split(" ").map { it.toInt() }
    val array = br.readLine().split(" ").map { it.toInt() }
    var answer = 0
    var intervalSum = 0
    var end = 0

    for(start in 0 until N) {
        while(intervalSum < M && end < N) {
            intervalSum += array[end]
            end++
        }

        if(intervalSum == M) answer ++

        intervalSum -= array[start]
    }

    print(answer)
}