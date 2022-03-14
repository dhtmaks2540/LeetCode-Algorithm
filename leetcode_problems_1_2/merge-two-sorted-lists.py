# 재귀 구조로 연결
def mergeTwoLists(list1, list2):
    # 값을 비교해 작은 값을 왼쪽으로
    if (not list1) or (list2 and list1.val > list2.val):
        list1, list2 = list2, list1
    
    if list1:
        # next를 통해 그 다음 값이 엮이도록 재귀 호출
        list1.next = self.mergeTwoLists(list1.next, list2)

    return list1