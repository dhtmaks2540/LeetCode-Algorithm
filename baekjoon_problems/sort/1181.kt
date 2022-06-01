import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val array = mutableSetOf<String>()
    repeat(n) { _ ->
        array.add(readLine())
    }

    var listArray = array.sorted()

    // 길이를 기준으로 정렬하는 Comparator
    val comparator = compareBy<String> { it.length }

    listArray = listArray.sortedWith (comparator)

    for(value in listArray) {
        println(value)
    }
}