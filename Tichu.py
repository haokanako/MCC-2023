def longest_run(N, K, cards):
    unique_cards = set(cards) #单一可能 这样比较好排序 1234567 
    max_run_length = 0
    for unique_integer in unique_cards:
        available_wildcards = K # 占位符
        current_run_length = 1
        for i in range(1, N): # 输出所有可能性
            next_integer = unique_integer + i

            if next_integer in unique_cards:
                current_run_length += 1
            elif available_wildcards > 0:
                available_wildcards -= 1
                current_run_length += 1
            else:
                break
        max_run_length = max(max_run_length, current_run_length)
    return max_run_length

# 这题我改变输入 把input删掉 因为最后我没跑出来。。。。
def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        N, K = map(int, lines[0].split())
        cards = list(map(int, lines[1].split()))
    result = longest_run(N, K, cards)
    print("最长", result)
if __name__ == "__main__":
    input_file_path = 'input.txt'
    process_file(input_file_path)
