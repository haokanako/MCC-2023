#非空子集
def all_non_empty_combinations(nums):
    n = len(nums)
    result = []

    for i in range(1, 1 << n):
        subset = [nums[j] for j in range(n) if (i >> j) & 1]
        result.append(subset)

    return result

N, K = map(int, input().split())
a = list(map(int, input().split()))
result = all_non_empty_combinations(a)

total_sum = 0
for subset in result:
    subset_sum = sum(subset)
    total_sum += subset_sum ** K #这里据说pow 会更快 但实际最后一个问题我没输出出来......

# 取摸
print(total_sum % 998244353)
