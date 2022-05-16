import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.ArrayDeque

const val MAX = 200 + 1

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val visited = Array<Array<Array<Boolean>>>(MAX) { Array(MAX) { Array(MAX) {false} } }
    val (A, B, C) = br.readLine().split(" ").map { it.toInt() }
    val queue = ArrayDeque<Triple<Int, Int, Int>>()
    val answer = mutableSetOf<Int>()
    queue.add(Triple(0, 0, C))

    while(queue.isNotEmpty()) {
        val (a, b, c) = queue.pollFirst()

        if(visited[a][b][c]) continue

        visited[a][b][c] = true

        if(a == 0) answer.add(c)

        if(a + b > B)
            queue.add(Triple(a + b - B, B, c))
        else
            queue.add(Triple(0, a + b, c))

        if(a + c > C)
            queue.add(Triple(a + c - C, b, C))
        else
            queue.add(Triple(0, b, a + c))

        if(b + a > A)
            queue.add(Triple(A, b + a - A, c))
        else
            queue.add(Triple(a + b, 0, c))

        if(b + c > C)
            queue.add(Triple(a, b + c - C, C))
        else
            queue.add(Triple(a, 0, b + c))

        if(c + a > A)
            queue.add(Triple(A, b, c + a - A))
        else
            queue.add(Triple(c + a, b, 0))

        if(c + b > B)
            queue.add(Triple(a, B, c + b - B))
        else
            queue.add(Triple(a, c + b, 0))
    }

    for(value in answer.sorted()) {
        print("$value ")
    }
}