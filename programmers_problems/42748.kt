fun solution(array: IntArray, commands: Array<IntArray>): IntArray {
        val answer = IntArray(commands.size)

        for((index, command) in commands.withIndex()) {
            val (i, j, k) = command

            val tempSortedArray = array.sliceArray(i-1 until j).sortedArray()
            answer[index] = tempSortedArray[k - 1]
        }

        return answer
    }