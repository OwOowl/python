# 딕셔너리 : key와 value 쌍으로 구성

dic1 = {1: 'a', 2: 'b', 3: 'c'}
print(dic1)

# 딕셔너리의 vlaue의 타입이 일치하지 않아도 됨
student1 = {'학번': 1000, '이름': '홍길동', '학과': '컴퓨터학과'}
print(student1)

# 지정한 key와 value 추가
student1['연락처'] = '010-1234-5678'
print(student1)

# 지정한 key의 value 값 수정
student1['학과'] = '파이썬학과'
print(student1)

# 지정된 key와 해당 value 값 삭제
del(student1['학과'])
print(student1)

# 지정된 key의 value 값 찾기
print(student1.get('이름'))
# 딕셔너리의 모든 key 값 가져오기
print(student1.keys())