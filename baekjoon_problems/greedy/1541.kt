import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val charArray = readLine().toCharArray()
    var prevOper = '+'
    var index = 0
    var answer = 0

    while(index < charArray.size) {
        if(charArray[index].isDigit()) {
            val sb = StringBuilder()
            while(index < charArray.size && charArray[index].isDigit()) {
                sb.append(charArray[index])
                index++
            }

            if(prevOper == '+')
                answer += sb.toString().toInt()
            else
                answer -= sb.toString().toInt()
        } else {
            if(charArray[index] == '-')
                prevOper = '-'

            index++
        }
    }

    println(answer)
}