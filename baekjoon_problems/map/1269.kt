import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.collections.HashMap
import kotlin.collections.HashSet

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (a, b) = readLine().split(" ").map { it.toInt() }
    val aArray = HashSet<Int>()
    val bArray = HashSet<Int>()
    val checkMap = HashMap<Int, Int>()

    var st = StringTokenizer(readLine(), " ")
    repeat(a) { _ ->
        aArray.add(st.nextToken().toInt())
    }

    st = StringTokenizer(readLine(), " ")
    repeat(b) { _ ->
        bArray.add(st.nextToken().toInt())
    }

    for(num in aArray) {
        checkMap[num] = 1
    }

    for(num in bArray) {
        if(!checkMap.containsKey(num))
            checkMap[num] = 1
        else
            checkMap[num] = checkMap.getOrDefault(num, 0).plus(1)
    }

    var answer = 0

    for(value in checkMap.values) {
        if(value == 1)
            answer++
    }

    println(answer)
}