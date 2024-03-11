# for 문을 이용해서 1~10 의 합 구하기

result = 0
for i in range(10):
    result += (i+1)
print(result)

# for 문을 이용하여 역순 출력
a = [1, 2, 3, 4, 5]
for i in range(1, len(a)+1):
    # print(a[-(i+1)])
    print(a[-i])
