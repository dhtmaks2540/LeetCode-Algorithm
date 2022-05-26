import java.io.BufferedReader
import java.io.InputStreamReader

fun main(args: Array<String>) = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val array = Array(n) { "" }
    repeat(n) { index ->
        array[index] = readLine()
    }
    var answer = 0

    for(i in 0 until n) {
        val visited = mutableMapOf<Char, Boolean>()
        var prev = array[i][0]
        visited[prev] = true
        var check = true

        for(j in 1 until array[i].length) {
            if(prev != array[i][j]) {
                if(visited.containsKey(array[i][j])) {
                    check = false
                    break
                } else {
                    visited[array[i][j]] = true
                    prev = array[i][j]
                }
            }
        }

        if(check) answer++
    }

    println(answer)
}