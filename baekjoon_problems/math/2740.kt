import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var st = StringTokenizer(readLine(), " ")
    val n = st.nextToken().toInt()
    val m = st.nextToken().toInt()
    val aGraph = Array(n) { IntArray(m) }

    repeat(n) { row ->
        st = StringTokenizer(readLine(), " ")
        repeat(m) { col ->
            aGraph[row][col] = st.nextToken().toInt()
        }
    }

    st = StringTokenizer(readLine(), " ")
    st.nextToken()
    val k = st.nextToken().toInt()
    val bGraph = Array(m) { IntArray(k) }

    repeat(m) { row ->
        st = StringTokenizer(readLine(), " ")
        repeat(k) { col ->
            bGraph[row][col] = st.nextToken().toInt()
        }
    }

    val resultGraph = Array(n) { IntArray(k) }

    for(i in 0 until n) {
        for(j in 0 until k) {
            var nowValue = 0
            for(z in 0 until m) {
                nowValue += aGraph[i][z] * bGraph[z][j]
            }
            resultGraph[i][j] = nowValue
        }
    }

    for(values in resultGraph) {
        for(value in values) {
            print("$value ")
        }
        println()
    }
}