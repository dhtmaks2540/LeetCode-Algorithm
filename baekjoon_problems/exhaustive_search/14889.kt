import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.math.abs
import kotlin.math.min
import kotlin.system.exitProcess

private var minDiff = Int.MAX_VALUE

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    // 점수 2차원 그래프
    val graph = Array(n) { IntArray(n) }
    // 방문을 확인하기 위한 리스트
    val visited = BooleanArray(n)

    repeat(n) { row ->
        val st = StringTokenizer(readLine(), " ")
        repeat(n) { col ->
            graph[row][col] = st.nextToken().toInt()
        }
    }

    // 차이를 계산하는 함수
    fun diff() {
        var startTeam = 0
        var linkTeam = 0
        
        // 만들어진 팀에서 조합을 계산
        for(i in 0 until n - 1) {
            for(j in i + 1 until n) {
                // i번째 사람과 j번째 사람을 방문했다면 스타트팀으로 점수 계산
                if(visited[i] && visited[j]) {
                    startTeam += graph[i][j]
                    startTeam += graph[j][i]
                }
                // i번째 사람과 j번째 사람을 방문하지 않았다면 링크팀으로 점수 계산
                else if(!visited[i] && !visited[j]) {
                    linkTeam += graph[i][j]
                    linkTeam += graph[j][i]
                }
            }
        }

        // 두 팀의 차이 계산
        val diff = abs(startTeam - linkTeam)

        // 점수가 0점이라면 최소 차이이므로 바로 출력
        if(diff == 0) {
            println(diff)
            exitProcess(0)
        }
        
        // 최소 차이 갱신
        minDiff = min(diff, minDiff)
    }

    // DFS 함수
    fun dfs(index: Int, cnt: Int) {
        // 팀이 나누어졌다면
        if(cnt == n / 2) {
            diff()
            return
        }

        for(i in index until n) {
            // 현재 선수를 방문하지 않았다면
            if(!visited[i]) {
                // 방문 처리 후 DFS 호출
                visited[i] = true
                dfs(i + 1, cnt + 1)
                // 다음을 위해 방문 처리 취소
                visited[i] = false
            }
        }
    }

    dfs(0, 0)
    println(minDiff)
}