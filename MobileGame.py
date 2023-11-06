def min_enemies_to_reach_power_level(T, test_cases):
    results = []
#做这个题的时候注意 同分数不能增加 
    for _ in range(T):
        N, A, B, enemies = test_cases[_]
        enemies.sort()
        num_kills = 0

        while A < B and len(enemies) > 0:
            left, right = 0, len(enemies) - 1
            idx_to_remove = -1
            while left <= right:#需要大量计算 所以我采用了 二分算法O(logn)科技 owo
                mid = (left + right) // 2
                if enemies[mid] < A:
                    idx_to_remove = mid
                    left = mid + 1
                else:
                    right = mid - 1

            if idx_to_remove != -1:
                A += enemies.pop(idx_to_remove)#这里是note提到的
                num_kills += 1
            else:
                break

        if A >= B:
            results.append(num_kills)
        else:
            results.append(-1)

    return results

T = int(input())
test_cases = []
for _ in range(T):
    N, A, B = map(int, input().split())
    enemies = list(map(int, input().split()))
    test_cases.append((N, A, B, enemies))

results = min_enemies_to_reach_power_level(T, test_cases)
for result in results:
    print(result)
