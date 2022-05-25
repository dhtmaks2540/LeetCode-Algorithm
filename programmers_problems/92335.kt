package programmers

import kotlin.math.sqrt

/**
 * 처음에는 에라토스테네스의 체와 스택을 사용해서 문제를 풀이하려고 헀는데, 에라토스테네스의 체 리스트 범위가
 * 너무 넓어서 숫자 하나하나씩 소수인지를 판별하는 방식으로 변경했다. 그리고 코틀린에는 x.toString(k)를 지정하면
 * 10진법 x의 수를 k 진법의 수롤 변경시켜준다. 이를 사용해서 n을 k진법의 수로 변경한 후 0을 기준으로 나누어준다.
 * 그리고 나누어진 수들을 파악하며 현재 값이 비어있지 않고, 소수이며, 양옆에 0을 포함하거나 또는 오른쪽에 0을 포함하거나
 * 또는 왼쪽에 0을 포함하거나 또는 숫자 혼자이면 filter를 통해 걸러내고 그 수를 파악하여 반환하는 방식으로 풀이했다.
 * 여기서 contains 메서드안에 문자열 템플릿을 사용하여 넣었는데 이런 방식으로도 코드가 가능하다...
 */

class Solution() {
    fun solution(n: Int, k: Int): Int {
        val changeN = n.toString(k)
        return changeN.split("0")
            .filter { value ->
            value.isNotEmpty()
                    && isPrime(value.toLong())
                    && (value.contains("0${value}0")
                    || value.contains("${value}0")
                    || value.contains("0${value}")
                    || value.contains(value))
        }.size
    }

    fun isPrime(n: Long): Boolean {
        if(n == 1L) return false
        else if(n == 2L) return true

        for(i in 2..sqrt(n.toDouble()).toLong()) {
            if (n % i == 0L) return false
        }

        return true
    }
}

fun main() {
    val result = solution(437674, 3)
    println(result)
}