import java.util.*

private fun solution42626(scoville: IntArray, k: Int): Int {
    var answer = 0
    val priorityQueue = PriorityQueue<Int>()

    scoville.forEach { value ->
        priorityQueue.add(value)
    }

    while(priorityQueue.isNotEmpty()) {
        if(priorityQueue.peek() >= k)
            return answer
        else {
            if(priorityQueue.size >= 2) {
                answer++

                val firstMinValue = priorityQueue.poll()
                val secondMinValue = priorityQueue.poll()
                val mixValue = firstMinValue + secondMinValue * 2
                priorityQueue.add(mixValue)
            } else
                break
        }
    }

    return -1
}