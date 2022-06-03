import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val array = readLine().toCharArray()
    val answer = HashSet<String>()

    for(i in array.indices) {
        for(j in i + 1..array.size) {
            // Concatenates characters in this CharArray into a String
            // start 인덱스부터 end 인덱스까지 CharArray의 요소들을 연결하여 String으로 변경
            answer.add(array.concatToString(i, j))
        }
    }

    println(answer.size)
}