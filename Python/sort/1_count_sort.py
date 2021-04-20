# 모든 원소의 값은 0보다 크거나 같아야 한다.
# 일반적으로 최댓값과 최솟값의 차이가 1,000,000을 넘지 않을 때 O(n + k)

array = [7, 5, 9, 0, 3, 1, 6, 1, 9, 10, 30, 3, 8, 20, 0, 5, 2]

result = []

# 모든 범위를 포함하는 리스트 선언 (0으로 초기화)
cnt_list = [0] * (max(array) + 1)

for i in range(len(array)):
    cnt_list[array[i]] += 1

for i in range(len(cnt_list)):
    for _ in range(cnt_list[i]):
        result.append(i)

print(result)
