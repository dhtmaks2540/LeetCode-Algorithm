class Solution {
    fun solution(answers: IntArray): IntArray {
        val answer = arrayListOf<Int>()

        val chrAnswers = answers.map { it.digitToChar() }
        val lenAnswer = chrAnswers.size

        val firstMan = StringBuilder("12345")
        val secondMan = StringBuilder("21232425")
        val thirdMan = StringBuilder("3311224455")

        repeat(lenAnswer / firstMan.length) { _ ->
            firstMan.append("12345")
        }

        repeat(lenAnswer / secondMan.length) { _ ->
            secondMan.append("21232425")
        }

        repeat(lenAnswer / thirdMan.length) { _ ->
            thirdMan.append("3311224455")
        }

        println(firstMan.toString())

        var firstManCnt = 0
        var secondManCnt = 0
        var thirdManCnt = 0

        for(index in 0 until lenAnswer) {
            if(firstMan[index] == chrAnswers[index])
                firstManCnt++
            if(secondMan[index] == chrAnswers[index])
                secondManCnt++
            if(thirdMan[index] == chrAnswers[index])
                thirdManCnt++
        }

        var maxCnt = Int.MIN_VALUE

        for((index, num) in intArrayOf(firstManCnt, secondManCnt, thirdManCnt).withIndex()) {
            if(num > maxCnt) {
                answer.clear()
                answer.add(index + 1)
                maxCnt = num
            } else if(num == maxCnt) {
                answer.add(index + 1)
            }
        }

        return answer.toIntArray()
    }
}