import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val num = readLine().toCharArray()
    val intNum = IntArray(num.size)
    for(index in num.indices) {
        intNum[index] = Character.getNumericValue(num[index])
    }

    intNum.sortDescending()
    for(num in intNum) {
        print("$num")
    }
}