import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val t = readLine().toInt()

    repeat(t) { _ ->
        val cloth = HashMap<String, Int>()

        val n = readLine().toInt()

        repeat(n) { _ ->
            val (clothName, clothType) = readLine().split(" ")
            if(!cloth.containsKey(clothType)) {
                cloth[clothType] = 1
            } else {
                cloth[clothType] = cloth.getOrDefault(clothType, 1).plus(1)
            }
        }

        var answer = 1

        for(value in cloth.values) {
            answer *= (value + 1)
        }

        println(answer - 1)
    }
}