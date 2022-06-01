import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.StringBuilder
import java.util.*
import kotlin.collections.HashMap

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val st = StringTokenizer(readLine(), " ")
    val array = IntArray(n) { st.nextToken().toInt() }
    val sortedArray = array.clone()
    sortedArray.sort()

    val rankingMap = HashMap<Int, Int>()
    var rank = 0

    for(value in sortedArray) {
        if(!rankingMap.containsKey(value)) {
            rankingMap[value] = rank++
        }
    }

    val sb = StringBuilder()

    for(key in array) {
        sb.append("${rankingMap[key]} ")
    }

    print(sb)
}