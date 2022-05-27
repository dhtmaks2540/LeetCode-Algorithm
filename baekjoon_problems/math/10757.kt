/**
 * 코틀린은 큰 숫자의 정수형을 사용할 때 BigInteger와 같은 타입이 있다.
 */

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (a, b) = readLine().split(" ").map { it.toBigInteger() }
    println(a + b)
}