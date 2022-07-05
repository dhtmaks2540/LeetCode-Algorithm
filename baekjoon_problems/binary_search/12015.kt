import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val st = StringTokenizer(readLine(), " ")
    val array = IntArray(n)
    repeat(n) { index ->
        array[index] = st.nextToken().toInt()
    }

    var cnt = 0
    val longestArray = IntArray(n)
    longestArray[0] = array[0]

    fun binarySearch(left: Int, right: Int, target: Int): Int {
        var start = left
        var end = right

        while(start < end) {
            val mid = start + (end - start) / 2

            if(target <= longestArray[mid])
                end = mid
            else
                start = mid + 1
        }

        return start
    }

    for(i in 1 until n) {
        if(longestArray[cnt] < array[i])
            longestArray[++cnt] = array[i]
        else {
            val index = binarySearch(0, cnt + 1, array[i])
            longestArray[index] = array[i]
        }
    }

    println(cnt + 1)
}