"""
숫자들을 섞어 30의 배수가 되는 가장 큰 수를 구하라

우선 30의 배수들을 적다보니 뒤에 숫자는 0으로 끝나고, 앞의 숫자는 3의 배수라는 것을 알았다.
이를 사용해서 주어진 숫자들을 정렬시키고 
1. 맨 뒤의 숫자가 0이 아니라면 30의 배수가 아니므로 -1
2. 그 앞부터 3의 배수가 아니라면 -1
3. 두 개 모두 해당하지 않는다면 30의 배수이므로 그 값을 출력하도록 풀이했다.

https://yoonsang-it.tistory.com/36

문제에서 주어진 값의 범위는 10^5으로 굉장히 큰 숫자이다. 따라서 완전 탐색등으로는 풀이할 수 없고
어떠한 규칙을 이용해서 풀이하고자 했다. 그 규칙이 위의 규칙인데 정확히 이야기하자면 30의 배수는
10의 배수이기도 하므로 0이 들어가있지 않다면 30의 배수가 될 수 없다. 따라서 우선 숫자에 0이 들어있는지
확인하고 들어있다면 남은 숫자의 각 자릿수 합이 3의 배수라면 3의 배수에 해당한다. 따라서 이를 사용해서
풀이하면된다.
"""

def solution():
    numbers = list(input())
    numbers.sort(reverse = True)

    if numbers[-1] != '0':
        print(-1)
    elif int("".join(numbers[:len(numbers)])) % 3 != 0:
        print(-1)
    else:
        print("".join(numbers))
        
def solution2():
    n = input()
    
    if '0' not in n:
        print(-1)
    else:
        num_sum = 0
        for i in range(len(n)):
            num_sum += int(n[i])
            
        if num_sum % 3 != 0:
            print(-1)
        else:
            sorted_num = sorted(n, reverse=True)
            print("".join(sorted_num))
            
solution2()