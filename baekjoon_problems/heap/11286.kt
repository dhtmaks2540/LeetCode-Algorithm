import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.Comparator
import kotlin.math.abs

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    // 최소힙을 구현하기 위한 람다식
    val lambda = {a: Int, b: Int -> when {
        a > b -> 1
        a < b -> -1
        else -> 0
    }}
    
    // 첫 번째를 비교한 후 두 번째를 비교하는 우선순위큐(하나가 아니라면 Comparator 필요)
    val pq = PriorityQueue(Comparator<Pair<Int, Int>> { a, b ->
        when {
            a.first != b.first -> lambda(a.first, b.first)
            else -> lambda(a.second, b.second)
        }
    })

    val sb = StringBuilder()

    repeat(n) { _ ->
        val x = readLine().toInt()
        if(x == 0) {
            if(pq.isEmpty())
                sb.append("0\n")
            else {
                val value = pq.poll()
                sb.append("${value.second}\n")
            }
        } else {
            pq.add(Pair(abs(x), x))
        }
    }

    println(sb.toString())
}