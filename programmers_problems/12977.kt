import kotlin.math.sqrt

class Solution {
    fun solution(nums: IntArray): Int {
        var answer = 0

        val MAX_NUM = 3000
        val primeNum = BooleanArray(MAX_NUM + 1) { true }

        for(i in 2..sqrt(MAX_NUM.toDouble()).toInt()) {
            if(primeNum[i]) {
                var j = 2
                while(i * j <= MAX_NUM) {
                    primeNum[i * j] = false
                    j++
                }
            }
        }

        for(i in 0 until nums.size - 2) {
            for(j in i + 1 until nums.size - 1) {
                for(k in j + 1 until nums.size)
                    if(primeNum[nums[i] + nums[j] + nums[k]])
                        answer++
            }
        }

        return answer
    }
}