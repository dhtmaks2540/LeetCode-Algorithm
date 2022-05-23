import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val target = readLine().toInt()
    val (A, B) = readLine().split(" ").map { it.toInt() }
    val arrayA = Array(A) { 0 }
    val arrayB = Array(B) { 0 }

    repeat(A) { index ->
        arrayA[index] = readLine().toInt()
    }

    repeat(B) { index ->
        arrayB[index] = readLine().toInt()
    }

    val subSumA = arrayListOf(0)
    val subSumB = arrayListOf(0)

    var low = 0
    var high = 0
    var intervalSum = 0

    while(low < A) {
        intervalSum += arrayA[high++]

        if(intervalSum <= target) {
            subSumA.add(intervalSum)
        }
        else {
           low++
           high = low
           intervalSum = 0
        }

        if(high == A) {
            high = 0
        }

        if((low == 0 && high == 0) || high + 1 == low) {
            low++
            high = low
            intervalSum = 0
        }
    }

    low = 0
    high = 0
    intervalSum = 0

    while(low < B) {
        intervalSum += arrayB[high++]

        if(intervalSum <= target) {
            subSumB.add(intervalSum)
        }
        else {
            low++
            high = low
            intervalSum = 0
        }

        if(high == B) {
            high = 0
        }

        if((low == 0 && high == 0) || high + 1 == low) {
            low++
            high = low
            intervalSum = 0
        }
    }

    subSumA.sort()
    subSumB.sort()

    var answer = 0

    fun lowerBound(target: Int): Int {
        var start = 0
        var end = subSumB.size

        while(end > start) {
            val mid = start + (end - start) / 2

            if(subSumB[mid] >= target) {
                end = mid
            }
            else {
                start = mid + 1
            }
        }

        return start
    }

    fun upperBound(target: Int): Int {
        var start = 0
        var end = subSumB.size

        while(end > start) {
            val mid = start + (end - start) / 2

            if(subSumB[mid] <= target) {
                start = mid + 1
            }
            else {
                end = mid
            }
        }

        return start
    }

    for(value in subSumA) {
        val lowIndex = lowerBound(target - value)
        val highIndex = upperBound(target - value)

        answer += highIndex - lowIndex
    }

    println(answer)
}