import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val t = br.readLine().toInt()
    val numbers = arrayOf(1,2,3)

    fun makeTarget(sumValue: Int, target: Int): Int {
        var answer = 0

        if(sumValue > target) return 0
        else if(sumValue == target) {
            return 1
        }

        var temp = sumValue

        for(number in numbers) {
            temp += number
            answer += makeTarget(temp, target)
            temp -= number
        }

        return answer
    }

    for(i in 0 until t) {
        val target = br.readLine().toInt()
        var answer = 0
        answer += makeTarget(0, target)
        println(answer)
    }
}