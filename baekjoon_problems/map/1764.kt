import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (N, M) = readLine().split(" ").map { it.toInt() }
    val personMap = HashMap<String, Int>()

    repeat(N) { _ ->
        val person = readLine()
        personMap[person] = 0
    }

    repeat(M) { _ ->
        val person = readLine()
        if(personMap.containsKey(person))
            personMap[person] = personMap.getOrDefault(person, 0) + 1
        else
            personMap[person] = 0
    }

    val answer = ArrayList<String>()

    for((key, value) in personMap.entries) {
        if(value == 1)
            answer.add(key)
    }

    answer.sort()
    println(answer.size)
    for(person in answer) {
        println(person)
    }
}