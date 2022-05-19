import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.sqrt

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val target = br.readLine().toInt()
    val primeNum = Array(target + 1) { true }

    for(i in 2..sqrt(target.toDouble()).toInt()) {
        if(primeNum[i]) {
            var j = 2
            while(i * j <= target) {
                primeNum[i * j] = false
                j++
            }
        }
    }

    val numbers = arrayListOf<Int>()
    for(i in 2 until primeNum.size) {
        if(primeNum[i]) numbers.add(i)
    }

    var answer = 0
    var end = 0
    var intervalSum = 0

    for(start in 0 until numbers.size) {
        while(intervalSum < target && end < numbers.size) {
            intervalSum += numbers[end]
            end++
        }

        if(intervalSum == target) answer++

        intervalSum -= numbers[start]
    }

    println(answer)
}