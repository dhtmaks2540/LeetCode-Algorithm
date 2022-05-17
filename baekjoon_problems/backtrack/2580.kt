import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.system.exitProcess

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val graph = Array<Array<Int>>(9) { Array(9) {0} }
    for(i in 0 until 9) {
        val st = StringTokenizer(br.readLine(), " ")
        for(j in 0 until 9) {
            graph[i][j] = st.nextToken().toInt()
        }
    }

    fun checkSudoku(row: Int, col: Int, num: Int): Boolean {
        for(index in 0 until 9) {
            if(graph[row][index] == num) return false
        }

        for(index in 0 until 9) {
            if(graph[index][col] == num) return false
        }

        val rowIndex = (row / 3) * 3
        val colIndex = (col / 3) * 3

        for(i in rowIndex..rowIndex + 2) {
            for(j in colIndex..colIndex + 2) {
                if(graph[i][j] == num) return false
            }
        }

        return true
    }

    fun dfsSudoku(row: Int, col: Int) {
        if(col == 9) {
            dfsSudoku(row + 1, 0)
            return
        }

        if(row == 9) {
            for(i in 0 until 9) {
                for(j in 0 until 9) {
                    print("${graph[i][j]} ")
                }
                println()
            }
            exitProcess(0)
        }

        if(graph[row][col] == 0) {
            for(i in 1..9) {
                if(checkSudoku(row, col, i)) {
                    graph[row][col] = i
                    dfsSudoku(row, col + 1)
                }
            }

            graph[row][col] = 0
            return
        }

        dfsSudoku(row, col + 1)
    }

    dfsSudoku(0, 0)
}