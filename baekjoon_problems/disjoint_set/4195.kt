import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max

const val MAX_VALUE = 200000 + 1

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))

    fun findParent(parent: Array<Int>, node: Int): Int {
        if(node == parent[node]) return node

        parent[node] = findParent(parent, parent[node])
        return parent[node]
    }

    fun unionParent(size: Array<Int>, parent: Array<Int>, node1: Int, node2: Int) {
        var node1Parent = findParent(parent, node1)
        var node2Parent = findParent(parent, node2)

        if(node1Parent != node2Parent) {
            if(size[node1Parent] < size[node2Parent]) {
                val temp = node1Parent
                node1Parent = node2Parent
                node2Parent = temp
            }

            parent[node2Parent] = node1Parent
            size[node1Parent] += size[node2Parent]
            size[node2Parent] = 0
        }
    }

    val T = br.readLine().toInt()

    for(i in 0 until T) {
        val F = br.readLine().toInt()
        val parent = Array(MAX_VALUE) {0}
        val size = Array(MAX_VALUE) {0}
        val nameMap = mutableMapOf<String, Int>()
        var idx = 1

        for(i in 0 until MAX_VALUE) {
            parent[i] = i
            size[i] = 1
        }

        for(i in 0 until F) {
            val (person1, person2) = br.readLine().split(" ")

            if(!nameMap.containsKey(person1)) {
                nameMap[person1] = idx++
            }

            if(!nameMap.containsKey(person2)) {
                nameMap[person2] = idx++
            }

            val person1Parent = findParent(parent, nameMap[person1]!!)
            val person2Parent = findParent(parent, nameMap[person2]!!)

            if(person1Parent == person2Parent) {
                println(max(size[person1Parent], size[person2Parent]))
            } else {
                unionParent(size, parent, person1Parent, person2Parent)
                println(max(size[person1Parent], size[person2Parent]))
            }
        }
    }
}