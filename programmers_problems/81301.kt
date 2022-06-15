fun solution(s: String): Int {
        val answer = StringBuilder()

        val numMap = hashMapOf<String, String>(
            "zero" to "0",
            "one" to "1",
            "two" to "2",
            "three" to "3",
            "four" to "4",
            "five" to "5",
            "six" to "6",
            "seven" to "7",
            "eight" to "8",
            "nine" to "9"
        )

        var index = 0
        while(index < s.length) {
            if(s[index].isDigit()) {
                answer.append(s[index])
                index++
            } else {
                val num = StringBuilder()
                while(index < s.length && !s[index].isDigit()) {
                    num.append(s[index])
                    index++

                    if(numMap.containsKey(num.toString())) {
                        answer.append(numMap[num.toString()])
                        break
                    }
                }
            }
        }

        return answer.toString().toInt()
    }