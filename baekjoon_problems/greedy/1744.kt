import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.collections.ArrayList

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    val posNum = ArrayList<Int>()
    val negNum = ArrayList<Int>()

    for(i in 0 until n) {
        val num = br.readLine().toInt()
        if(num <= 0) negNum.add(num)
        else posNum.add(num)
    }

    var answer = 0

    posNum.sortDescending()
    negNum.sort()

    val tempStack = Stack<Int>()

    for(num in posNum) {
        when {
            num == 1 -> {
                answer += 1
            }
            tempStack.isEmpty() -> {
                tempStack.add(num)
            }
            else -> {
                answer += num * tempStack.pop()
            }
        }
    }

    if(tempStack.isNotEmpty()) {
        answer += tempStack.pop()
    }

    for(num in negNum) {
        when {
            tempStack.isEmpty() -> {
                tempStack.add(num)
            }
            else -> {
                answer += num * tempStack.pop()
            }
        }
    }

    if(tempStack.isNotEmpty()) {
        answer += tempStack.pop()
    }

    println(answer)
}