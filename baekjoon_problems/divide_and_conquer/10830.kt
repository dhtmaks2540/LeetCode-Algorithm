import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var st = StringTokenizer(readLine(), " ")
    val n = st.nextToken().toInt()
    val b = st.nextToken().toLong()
    val graph = Array(n) { IntArray(n) }
    repeat(n) { row ->
        st = StringTokenizer(readLine(), " ")
        repeat(n) { col ->
            graph[row][col] = st.nextToken().toInt()
        }
    }

    fun pow(nowGraph: Array<IntArray>, exponent: Long): Array<IntArray> {
        if(exponent == 1L) {
            for(i in 0 until n) {
                for(j in 0 until n) {
                    graph[i][j] %= 1000
                }
            }

            return graph
        }

        val tempGraph = pow(nowGraph, exponent / 2)
        val evenGraph = Array(n) { IntArray(n) }

        for(i in 0 until n) {
            for(j in 0 until n) {
                var nowValue = 0
                for(k in 0 until n) {
                    nowValue += tempGraph[i][k] * tempGraph[k][j]
                }
                evenGraph[i][j] = nowValue % 1000
            }
        }

        if(exponent % 2 == 1L) {
            val ordGraph = Array(n) { IntArray(n) }
            for(i in 0 until n) {
                for(j in 0 until n) {
                    var nowValue = 0
                    for(k in 0 until n) {
                        nowValue += evenGraph[i][k] * graph[k][j]
                    }
                    ordGraph[i][j] = nowValue % 1000
                }
            }

            return ordGraph
        }

        return evenGraph
    }

    val resultGraph = pow(graph, b)
    resultGraph.forEach { values ->
        values.forEach { value ->
            print("$value ")
        }
        println()
    }
}