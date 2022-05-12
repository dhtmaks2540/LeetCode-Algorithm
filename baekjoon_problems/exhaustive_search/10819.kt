import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.math.abs
import kotlin.math.max

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    val array = br.readLine().split(" ").map { it.toInt() }
    var maxValue = Int.MIN_VALUE

    fun recursive(visited: Array<Boolean>, path: Stack<Int>) {
        if(path.size == n) {
            var sumValue = 0
            for(i in 1 until n) {
                sumValue += abs(path[i - 1] - path[i])
            }
            maxValue = max(maxValue, sumValue)
        }

        for(i in 0 until n) {
            if(!visited[i]) {
                visited[i] = true
                path.add(array[i])
                recursive(visited, path)
                visited[i] = false
                path.pop()
            }
        }
    }
    val visited = Array(n) { false }
    recursive(visited, Stack())
    println(maxValue)
}