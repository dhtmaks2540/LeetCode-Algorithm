import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val numbers = br.readLine()

    if(numbers.any { it == '0' }) {
        var numSum = 0
        for(number in numbers) {
            numSum += number.digitToInt()
        }

        if(numSum % 3 != 0) {
            print(-1)
        } else {
            val sortedNum = numbers.toList().sortedDescending()
            sortedNum.forEach { print(it) }
        }
    } else {
        print(-1)
    }
}