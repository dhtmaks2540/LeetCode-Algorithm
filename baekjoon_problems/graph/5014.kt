import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (F, S, G, U, D) = br.readLine().split(" ").map { it.toInt() }
    val visited = Array(F + 1) { -1 }
    val queue = ArrayDeque<Int>()
    queue.add(S)
    visited[S] = 0

    while(queue.isNotEmpty()) {
        val now = queue.pollFirst()

        if((now + U in 1..F) && visited[now + U] == -1) {
            queue.add(now + U)
            visited[now + U] = visited[now] + 1
        }

        if((now - D in 1..F) && visited[now - D] == -1) {
            queue.add(now - D)
            visited[now - D] = visited[now] + 1
        }
    }

    if(visited[G] == -1) println("use the stairs")
    else println(visited[G])
}