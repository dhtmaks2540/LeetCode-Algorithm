import math

"""
주차장을 사용한 차의 정보를 입력받아 해당 차에 대한 요금을 출력하는 문제로,
차 번호를 key로 하여 정보를 저장하고 IN - OUT을 분기하여 그 상황에 맞게 처리한다.
그 후 계산된 시간을 가지고 금액을 정산한 후 결과로 출력하였다. 
따라서 이 문제는 HashTable 자료구조를 사용해서 key-Value 형식으로 값을 저장하여 처리하면 되는 문제
이다.

"""

def solution(fees, records):
    # 시간 계산하는 메서드
    def check_time(record_time, now_time):
        record_time = record_time.split(":")
        now_time = now_time.split(":")
        
        now_value = int(now_time[0]) * 60 + int(now_time[1])
        record_value = int(record_time[0]) * 60 + int(record_time[1])
        
        result_time = now_value - record_value
        return result_time

    # 차의 입출력 정보를 저장하는 Map
    car_dict = dict()
    # 차의 시간을 저장하는 Map
    car_time = dict()
    
    for record in records:
        time, car_num, type = record.split(" ")
        
        # 처음 온 차라면 기록
        if car_num not in car_dict:
            car_time[car_num] = 0
        # 나가는 경우 -> 정산처리
        elif type == "OUT":
            result_time = check_time(car_dict[car_num][0], time)
            car_time[car_num] += result_time
        # 차 정보 등록
        car_dict[car_num] = (time, type)
            
    # 마지막으로 확인하면서 out 처리가 안된 자동차 계산
    for key in car_dict.keys():
        if car_dict[key][1] == "IN":
            result_time = check_time(car_dict[key][0], "23:59")
            car_time[key] += result_time
            
    answer = []
    
    # 금액 계산
    for key, value in car_time.items():
        if value > fees[0]:
            money = fees[1] + math.ceil((value - fees[0]) / fees[2]) * fees[3]
        else:
            money = fees[1]
        
        answer.append((key, money))
    
    # 차량번호를 기준으로 정렬 후 결과 반환
    answer.sort()
            
    return [item[1] for item in answer]

fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
result = solution(fees, records)
print(result)