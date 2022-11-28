# 튜플
tt1 = (10, 20, 30, 40)
print(tt1[0])
print(tt1[1])
print(tt1[2])
print(tt1[3])

# 튜플[a:b] : a 와 b 인덱스 사이의 값 출력
print(tt1[1:3])
# 튜플[a:] : a 인덱스 이후의 값 출력
print(tt1[1:])
# 튜플[:a] : a 인덱스 이전까지의 값 출력
print(tt1[:3])

# 두 개의 튜플 합성
tt2 = ('A', 'B')
print(tt1 + tt2)

# 튜플값 복사
print(tt2 * 3)

tt3 = ((1, 2, 3),
       (4, 5, 6),
       (7, 8, 9))
for i in tt3 :
    print(i)

print()

# 튜플 -> 리스트
myTuple = (10, 20, 30)
myList = list(myTuple)
myList.append(40)
for i in myList:
    print(i)

myTuple = tuple(myList)
for i in myTuple:
    print(i)