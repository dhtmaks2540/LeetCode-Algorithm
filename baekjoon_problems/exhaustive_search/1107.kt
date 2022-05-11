import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.collections.ArrayList
import kotlin.math.abs
import kotlin.math.min

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))

    val n = br.readLine().toInt()
    val m = br.readLine().toInt()

    var disableNum: List<Int> = ArrayList()
    var answer = abs(n - 100)

    disableNum = if(m != 0) {
        br.readLine().split(" ").map { it.toInt() }
    } else {
        arrayListOf()
    }


    for(i in 0..1000000) {
        var check = true
        for(j in i.toString()) {
            if(disableNum.contains(Character.getNumericValue(j))) {
                check = false
                break
            }
        }

        if(check) {
            answer = min(answer, i.toString().length + abs(i - n))
        }
    }

    println(answer)
}