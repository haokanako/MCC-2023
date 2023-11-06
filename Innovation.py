#  这题花了我很多思考时间，起初我还以为是题出错了
# 一定要记得 要判断themax 就是数组里子数组最大和，他一定是在最后一个的 然后重新排序 求出m-1的所有子列表的前两个数字和
# 但是最后我还是有没做出来的
def innovation(n, m, test_cases):
    max_lists = sorted(test_cases,key=sum, reverse=True)
    sorted_lists = sorted(test_cases, key=lambda x: x[0] + x[1], reverse=True)
    print(sorted_lists[:m-1])
    themax = max_lists[0]
    #如果themax 在sorted_lists的前m-1个子列表中
    #if themax in sorted_lists[:m-1]:
    sorted_lists.remove(themax)
    sum_lists = sum([sum(x[:2]) for x in sorted_lists[:m-1]])
    return sum_lists + sum(themax)


n, m = map(int, input().split())
test_cases = []
for _ in range(n):
    cardnumbers = list(map(int, input().split()))
    test_cases.append(cardnumbers)
print(innovation(n, m, test_cases))
