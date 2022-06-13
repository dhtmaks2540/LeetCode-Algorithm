import java.util.*
import kotlin.collections.ArrayList

class Solution {
    fun solution(new_id: String): String {
        // 1단계
        var answer: String = new_id.lowercase()
        var newId = answer.toMutableList()
        val temp = ArrayList<Char>()
        val correctSymbol = "-_."

        // 2단계
        newId.forEach {
            if(it.isDigit() || it.isLetter() || it in correctSymbol)
                temp.add(it)
        }

        newId = temp.toMutableList()


        // 3단계
        val tempStack = Stack<Char>()
        newId.forEach {
            if(tempStack.isNotEmpty() && tempStack[tempStack.lastIndex] == '.' && it == '.') {
                tempStack.pop()
            }

            tempStack.add(it)
        }

        newId = tempStack.toMutableList()

        // 4단계
        var index = 0
        while(index < newId.size) {
            if(index == 0) {
                if (newId[index] == '.')
                    newId.removeAt(0)
            }
            else if(index == newId.lastIndex) {
                    if(newId[index] == '.') {
                        println("YES")
                        newId.removeAt(newId.lastIndex)
                    }
                }

            index++
        }

        // 5단계
        if(newId.isEmpty())
            newId.add('a')

        // 6단계
        if(newId.size >= 16) {
            while(newId.size > 15 || newId.last() == '.') {
                newId.removeAt(newId.lastIndex)
            }
        }

        // 7단계
        if(newId.size <= 2) {
            while(newId.size <= 2) {
                newId.add(newId.last())
            }
        }

        println(newId.joinToString(""))
        return newId.toString()
    }
}