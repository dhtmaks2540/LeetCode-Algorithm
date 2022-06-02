import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (N, M) = readLine().split(" ").map { it.toInt() }
    val sMap = HashMap<String, Int>()

    repeat(N) { _ ->
        val value = readLine()
        sMap[value] = 0
    }

    repeat(M) { _ ->
        val value = readLine()
        if(sMap.containsKey(value)) {
            sMap[value] = sMap.getOrDefault(value, 0) + 1
        }
    }

    var answer = 0

    for(value in sMap.values) {
        answer += value
    }

    println(answer)
}