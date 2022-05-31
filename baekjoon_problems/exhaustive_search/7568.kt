package baekjoon

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val array = ArrayList<Pair<Int, Int>>()
    for(i in 0 until n) {
        val (wei, hei) = readLine().split(" ").map { it.toInt() }
        array.add(Pair(wei, hei))
    }

    val answer = IntArray(n) { 0 }

    for(i in 0 until n) {
        var cnt = 0
        for(j in 0 until n) {
            if(i != j) {
                if(array[i].first < array[j].first && array[i].second < array[j].second)
                    cnt++
            }
        }
        answer[i] = cnt + 1
    }

    for(value in answer) {
        print("$value ")
    }
}