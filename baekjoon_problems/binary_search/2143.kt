import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val T = readLine().toInt()
    val A = readLine().toInt()

    val arrayA = Array(A) { 0 }
    var st = StringTokenizer(readLine(), " ")
    for(i in 0 until A) {
        arrayA[i] = st.nextToken().toInt()
    }

    val B = readLine().toInt()
    val arrayB = Array(B) { 0 }
    st = StringTokenizer(readLine(), " ")
    for(i in 0 until B) {
        arrayB[i] = st.nextToken().toInt()
    }

    val subSumA = arrayListOf<Int>()
    var subSumB = arrayListOf<Int>()

    var start = 0
    var end = 0
    var intervalSum = 0

    while(start < A) {
        while(end < A) {
            intervalSum += arrayA[end++]
            subSumA.add(intervalSum)
        }

        start += 1
        end = start
        intervalSum = 0
    }

    start = 0
    end = 0
    intervalSum = 0

    while(start < B) {
        while(end < B) {
            intervalSum += arrayB[end++]
            subSumB.add(intervalSum)
        }

        start += 1
        end = start
        intervalSum = 0
    }

    var answer = 0
    subSumA.sort()
    subSumB.sort()

    fun lowerBound(target: Int): Int {
        var start = 0
        var end = subSumB.size

        while(end > start) {
            val mid = start + (end - start) / 2

            if(subSumB[mid] >= target) {
                end = mid
            } else {
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
            } else {
                end = mid
            }
        }

        return start
    }

    for(value in subSumA) {
        val lowerIndex = lowerBound(T - value)
        val upperIndex = upperBound(T - value)

        answer += (upperIndex - lowerIndex)
    }

    println(answer)
}