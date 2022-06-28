import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val array = IntArray(n)
    var st = StringTokenizer(readLine(), " ")
    repeat(n) { index ->
        array[index] = st.nextToken().toInt()
    }
    array.sort()

    val m = readLine().toInt()
    val targetArray = IntArray(m)
    st = StringTokenizer(readLine(), " ")
    repeat(m) { index ->
        targetArray[index] = st.nextToken().toInt()
    }

    fun binarySearch(s: Int, e: Int, target: Int): Int {
        var start = s
        var end = e
        while(start <= end) {
            val mid = start + (end - start) / 2

            when {
                array[mid] == target -> return mid
                array[mid] > target -> end = mid - 1
                else -> start = mid + 1
            }
        }

        return -1
    }

    val start = 0
    val end = n - 1
    val sb = StringBuilder()

    for(target in targetArray) {
        val index = binarySearch(start, end, target)
        if(index == -1)
            sb.append("0\n")
        else
            sb.append("1\n")
    }

    println(sb.toString())
}