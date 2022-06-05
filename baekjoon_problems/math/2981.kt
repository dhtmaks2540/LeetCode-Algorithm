import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.sqrt

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val array = IntArray(n)
    repeat(n) { index ->
        array[index] = readLine().toInt()
    }

    fun findGCD(a: Int, b: Int): Int {
        var gcdNum = a
        var divideNum = b
        var remainder = b

        while(remainder != 0) {
            remainder = gcdNum % divideNum
            gcdNum = divideNum
            divideNum = remainder
        }

        return gcdNum
    }
    
    array.sort()
    
    var gcdValue = array[1] - array[0]
    
    for(i in 2 until n) {
        gcdValue = findGCD(gcdValue, array[i] - array[i - 1])
    }
    
    val answer = HashSet<Int>()
    
    for(i in 2..sqrt(gcdValue.toDouble()).toInt()) {
        if(gcdValue % i == 0) {
            answer.add(i)
            answer.add(gcdValue / i)
        }
    }
    
    answer.add(gcdValue)
    
    for(value in answer.sorted()) {
        print("$value ")
    }
}