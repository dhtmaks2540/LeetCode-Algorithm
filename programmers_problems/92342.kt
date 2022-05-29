class Solution {
    private var maxScore = 0

    fun solution(n: Int, info: IntArray): IntArray {
    var answer: IntArray = intArrayOf()
    fun checkScore(ryan: Array<Int>): Int {
        var score = 0
        for(i in 0..10) {
            if(ryan[i] == info[i] && info[i] == 0)
                continue
            else if(ryan[i] > info[i])
                score += 10 - i
            else
                score -= 10 - i
        }

        return score
    }

    fun dfs(index: Int, cnt: Int, ryan: Array<Int>) {
        if(index == -1 && cnt != 0)
            return

        if(cnt == 0) {
            val score = checkScore(ryan)
            if(maxScore < score) {
                answer = ryan.toIntArray()
                maxScore = score 
            }
            return
        }

        // 가장 낮은 점수부터 가장 높은 점수 순으로 화살을 쏴서
        // 점수가 같은 것이 여러개일 경우 낮은 점수 더 많이 쏜걸로 출력되도록 처리
        for(i in cnt downTo 0) {
            ryan[index] = i
            dfs(index - 1, cnt - i, ryan)
            ryan[index] = 0
        }
    }

    val ryan = Array(11) { 0 }
    dfs(10, n, ryan)

    return if(maxScore == 0)
        intArrayOf(-1)
    else
        answer
    }
}