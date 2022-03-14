import collections

def groupAnagrams(strs):
    # defaultdict 생성
    # 키가 없어도 keyError가 발생하지 않고 디폴트 값을 기준으로
    # 해당 키에 대한 딕셔너리 아이템 생성해줌
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리에 추가(정렬하면 키가 같아지기에)
        # join을 사용하여 리스트를 문자열로
        anagrams[''.join(sorted(word))].append(word)
    
    # 딕셔너리의 value 반환
    return list(anagrams.values())