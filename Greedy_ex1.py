# 예제 1 거스름돈
n = int(input())
money_type = [500, 100, 50, 10]
result = 0

for i in money_type:
    result += n // i
    n %= i

print(result)