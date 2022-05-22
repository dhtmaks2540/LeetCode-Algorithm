import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (N, S) = readLine().split(" ").map { it.toInt() }
    val array = readLine().split(" ").map { it.toInt() }
    val subSum = mutableMapOf<Int, Int>()
    var cnt = 0L

    fun rightSeq(mid: Int, sum: Int) {
        if(mid == N) {
            subSum[sum] = subSum.getOrDefault(sum, 0) + 1
            return
        }

        rightSeq(mid + 1, sum + array[mid])
        rightSeq(mid + 1, sum)
    }

    fun leftSeq(st: Int, sum: Int) {
        if(st == N / 2) {
            cnt += subSum.getOrDefault(S - sum, 0)
            return
        }

        leftSeq(st + 1, sum + array[st])
        leftSeq(st + 1, sum)
    }

    rightSeq(N / 2, 0)
    leftSeq(0, 0)

    if(S == 0) println(cnt - 1)
    else println(cnt)
}