import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (L, C) = br.readLine().split(" ").map { it.toInt() }
    val array = br.readLine().split(" ").sorted()
    val lenArray = array.size
    val vowelArray = arrayOf('a', 'e', 'i', 'o', 'u')
    val answer = ArrayList<String>()

    fun checkCanPassword(password: String): Boolean {
        var consonantCnt = 0
        var vowelCnt = 0

        for(x in password) {
            if(vowelArray.contains(x)) vowelCnt++
            else consonantCnt++

            if(consonantCnt >= 2 && vowelCnt >= 1) return true
        }

        return false
    }

    fun dfs(index: Int, password: String) {
        if(password.length == L && checkCanPassword(password)) {
            answer.add(password)
            return
        }

        for(i in index until lenArray) dfs(i + 1, password + array[i])
    }

    dfs(0, "")

    for(x in answer) {
        println(x)
    }
}