"""
이동하려는 채널 까지 최소 버튼을 몇 번 눌러야 하는지 구하라.

이동하려는 채널로 이동하기 위해서 100에서 원하는 숫자까지 +, -를 통해 이동한 횟수와
사용하지 않는 숫자들을 제외하고 숫자 버튼을 눌러 원하는 숫자와 가장 가까운 숫자로 이동한 후
그 숫자부터 +, -를 통해 이동한 횟수 중 최솟값을 출력하여 문제를 풀이하였다. 즉,
완전 탐색을 통해 주어진 숫자 500,000 * 2까지의 숫자를 모두 탐색하면서 현재 숫자가 모두
사용할 수 있는 숫자이며, 주어진 숫자와의 차이가 최소라면 이를 계속해서 저장해나갔다.

처음에는 각 자릿수에서 가까운 숫자를 찾으려고 했는데 정답이 나오지 않는 예외 사항이 발생해서
문제에서 주어진 범위의 최대값인 500,000의 * 2한 값인 1,000,000까지 탐색하면서 모두 사용할 수 있는
숫자인지 판별하며 차이를 최소로 하도록 풀이하는 방식으로 변경했다.
"""

def solution():
    import sys

    # 이동하려는 채널
    N = int(sys.stdin.readline().strip())
    # 고장난 버튼의 개수
    M = int(sys.stdin.readline().strip())
    # 사용 불가능한 숫자
    if M != 0:
        disable_nums = sys.stdin.readline().strip().split(" ")
    else:
        disable_nums = list()

    # 직접 +, -를 사용해서 이동한 경우에 버튼을 누른 횟수
    answer = abs(N - 100)

    for num in range(0, 1000001):
        check = True
        for ch in str(num):
            if ch in disable_nums:
                check = False
                break
            
        if check:
            answer = min(answer, len(str(num)) + abs(num - N))
            
    print(answer)
    
solution()