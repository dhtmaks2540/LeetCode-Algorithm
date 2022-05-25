package programmers

/**
 * 이용자의 ID와 신고한 이용자의 ID 정보가 담긴 문자열 배열이 주어지므로
 * 이를 map을 통해 저장하는데, 하나는 이용자의 ID를 key로하고 신고 성공 횟수를 value로 하여 선언하고,
 * 하나는 이용자의 ID를 key로하고 해당 ID를 신고한 사람들을 value로 설정한다.
 * 이제 이용자의 ID에 그 ID를 신고한 사람들이 기록되어 있으므로 신고횟수가 K개 이상이라면
 * 신고에 성공한 사람들의 Count를 증가시키는 방식으로 풀이했다.
 */

class Solution {
    fun solution(id_list: Array<String>, report: Array<String>, k: Int): IntArray {
        val reportDic = mutableMapOf<String, MutableSet<String>>()
        val reportNum = mutableMapOf<String, Int>()

        for(id in id_list) {
            reportDic[id] = mutableSetOf()
            reportNum[id] = 0
        }

        for(value in report) {
            val (fromPerson, toPerson) = value.split(" ")
            reportDic[toPerson]?.add(fromPerson)
        }

        for(value in reportDic.values) {
            if(value.size >= k) {
                for(fromPerson in value) {
                    reportNum[fromPerson] = reportNum[fromPerson]!!.plus(1)
                }
            }
        }

        return reportNum.values.toIntArray()
    }
}

fun main() {
    val sol = Solution()
    val idList = arrayOf("muzi", "frodo", "apeach", "neo")
    val reportList = arrayOf("muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi")
    val k = 2

    val result = sol.solution(idList, reportList, k)
    for(x in result) print("$x ")
}