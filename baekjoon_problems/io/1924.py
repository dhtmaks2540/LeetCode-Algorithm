"""
https://truman.tistory.com/81

달력을 이용할 수 있나
"""

def solution():
    # 월과 일
    x, y = map(int, input().split(" "))
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    day_of_week = ['SUN', 'MON', "TUE", 'WED', "THU", 'FRI', 'SAT']

    days = y
    
    for i in range(x - 1):
        days += months[i]
        
    print(day_of_week[days % 7])
    
solution()
    
    
# 라이브러리 사용
def solution2():
    import datetime
    
    day_of_week = ['MON', "TUE", 'WED', "THU", 'FRI', 'SAT', 'SUN']
    
    x, y = map(int, input().split(" "))
    target_date = datetime.date(2007, x, y)
    print(day_of_week[target_date.weekday()])
    
# solution2()