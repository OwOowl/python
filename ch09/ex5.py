
# *가변인수
def para_func(*para):
    result = 0
    for num in para:
        result += num
    return result


hap = para_func(10, 20)
print(hap)
hap = para_func(10, 20, 30)
print(hap)
hap = para_func(10, 20, 30, 40)
print(hap)

