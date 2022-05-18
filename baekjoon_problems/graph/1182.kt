import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (N, S) = br.readLine().split(" ").map { it.toInt() }
    val array = br.readLine().split(" ").map { it.toInt() }
    var answer = 0

    fun dfs(index: Int, path: Stack<Int>) {
        if(!path.empty() && path.sum() == S) {
            answer++
        }

        for(i in index until N) {
            path.add(array[i])
            dfs(i + 1, path)
            path.pop()
        }
    }

    dfs(0, Stack())
    println(answer)
}