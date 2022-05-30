import kotlin.math.max

private var maxSheep = 0

fun solution(info: IntArray, edges: Array<IntArray>): Int {
    val graph = Array(info.size) { ArrayList<Int>() }
    val visited = Array(info.size) { false }
    edges.forEach { edge ->
        graph[edge[0]].add(edge[1])
    }

    fun findMaxRecursive(currentNode: Int, visited: Array<Boolean>, cntSheep: Int, cntWolf: Int, canGo: ArrayList<Int>) {
        var nowCntWolf = cntWolf
        var nowCntSheep = cntSheep
        if(visited[currentNode]) return
        visited[currentNode] = true

        if(info[currentNode] == 1) nowCntWolf += 1
        else {
            nowCntSheep++
            maxSheep = max(nowCntSheep, maxSheep)
        }

        if(nowCntWolf >= nowCntSheep) return

        canGo.addAll(graph[currentNode])

        for(nextNode in canGo) {
            val tempList = arrayListOf<Int>()
            for(loc in canGo) {
                if(loc != nextNode && !visited[nextNode])
                    tempList.add(loc)
            }
            findMaxRecursive(nextNode, visited.copyOf(), nowCntSheep, nowCntWolf, canGo = tempList)
        }
    }

    findMaxRecursive(0, visited, 0, 0, arrayListOf())

    return maxSheep
}