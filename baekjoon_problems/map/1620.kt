import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Exception

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (N, M) = readLine().split(" ").map { it.toInt() }
    val pokemonMap = HashMap<String, Int>()
    val numList = ArrayList<String>()

    repeat(N) { index ->
        val value = readLine()
        pokemonMap[value] = index + 1
        numList.add(value)
    }

    repeat(M) { _ ->
        var value = readLine()
        try {
            val numValue = value.toInt()
            println(numList[numValue - 1])
        } catch(e: Exception) {
            println(pokemonMap[value])
        }
    }
}