import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (E, S, M) = br.readLine().split(" ").map { it.toInt() }

    var eCount = 1
    var sCount = 1
    var mCount = 1
    var answer = 1

    while(eCount != E || sCount != S || mCount != M) {
        eCount++
        sCount++
        mCount++

        if(eCount >= 16) eCount = 1
        if(sCount >= 29) sCount = 1
        if(mCount >= 20) mCount = 1

        answer++
    }

    println(answer)
}