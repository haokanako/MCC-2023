def dragon_sum(n, k, integers):
    for _ in range(k):
        for i in range(n):
            num = integers[i]
            if num % 2 == 0:
                integers[i] = num >> 1  # 使用位运算右移代替整除2
            else: #tips: 实际测试 用位运算并没有得到速度提升
                integers[i] = 3 * num + 1
    return sum(integers)

n, k = map(int, input().split())
integers = list(map(int, input().split()))
result = dragon_sum(n, k, integers)
print(result)


