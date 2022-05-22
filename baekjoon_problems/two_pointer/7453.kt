import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val array = Array(4) { Array(n) { 0 } }

    repeat(n) { i ->
        val st = StringTokenizer(readLine(), " ")
        repeat(4) { index ->
            array[index][i] = st.nextToken().toInt()
        }
    }

    val leftArray = Array(n * n) { 0 }
    val rightArray = Array(n * n) { 0 }

    for(i in 0 until n) {
        for(j in 0 until n) {
            leftArray[i * n + j] = array[0][i] + array[1][j]
            rightArray[i * n + j] = array[2][i] + array[3][j]
        }
    }

    leftArray.sort()
    rightArray.sort()

    var i = 0
    var j = n * n - 1
    var answer = 0L

    while(i < n * n && j >= 0) {
        when {
            leftArray[i] + rightArray[j] == 0 -> {
                var nextI = i + 1
                var nextJ = j - 1

                while(nextI < n * n && leftArray[i] == leftArray[nextI])
                    nextI++
                while(nextJ >= 0 && rightArray[j] == rightArray[nextJ])
                    nextJ--

                answer += (nextI - i) * (j - nextJ)
                i = nextI
                j = nextJ
            }
            leftArray[i] + rightArray[j] > 0 -> {
                j--
            }
            else -> {
                i++
            }
        }
    }

    println(answer)
}