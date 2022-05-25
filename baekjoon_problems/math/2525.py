# 현재 시, 분
now_hour, now_min = map(int, input().split(" "))
# 요리에 필요한 시간(분)
need_min = int(input())

# 요리에 필요한 시간 계산
need_hour = need_min // 60
# 분 계산
need_min %= 60

now_hour += need_hour
now_min += need_min

# 만약 60분이 넘었다면
if now_min >= 60:
    now_min -= 60
    now_hour += 1

# 만약 24시가 넘었다면
if now_hour >= 24:
    now_hour -= 24
    
print(now_hour, now_min)