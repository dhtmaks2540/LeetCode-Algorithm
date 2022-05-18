import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))

    fun dfs(nums: List<Int>, index: Int, path: Stack<Int>) {
        if(path.size == 6) {
            for(x in path) {
                print("$x ")
            }
            println()
            return
        }

        for(i in index until nums.size) {
            path.add(nums[i])
            dfs(nums, i + 1, path)
            path.pop()
        }
    }

    while(true) {
        val values = br.readLine().split(" ").map { it.toInt() }
        if(values[0] == 0) break

        val k = values[0]
        val nums = values.subList(1, values.size).sorted()
        dfs(nums, 0, Stack())
        println()
    }
}