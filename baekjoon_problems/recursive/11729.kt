import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.StringBuilder
import kotlin.math.pow

private lateinit var sb: StringBuilder

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    // 원판의 개수
    val n = br.readLine().toInt()
    sb = StringBuilder()
    sb.append("${2.0.pow(n.toDouble()).toInt() - 1}\n")
    recursiveHanoi(1, 3, n)
    print(sb)
}

fun recursiveHanoi(fromLoc: Int, toLoc: Int, n: Int) {
    // 원판이 한 개라면 옮기기
    if(n == 1) {
        sb.append("$fromLoc $toLoc\n")
        return
    }

    val empty = 6 - fromLoc - toLoc

    // 1 단계(n-1개의 원판을 empty로)
    recursiveHanoi(fromLoc, empty, n - 1)
    // 2 단계(남은 1개의 원판을 toLoc으로)
    sb.append("$fromLoc $toLoc\n")
    // 3 단계(n-1개의 원판을 empty에서 toLoc으로)
    recursiveHanoi(empty, toLoc, n - 1)
}