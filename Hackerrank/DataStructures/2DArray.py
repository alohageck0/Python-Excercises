arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)


def count_hourglass(start):
    summ = arr[start][start] + arr[start][start + 1] + arr[start][start + 2] + arr[start + 1][start + 1] + \
           arr[start + 2][start] + arr[start + 2][start + 1] + arr[start + 2][start + 2]
    return summ


num = 0
result = 0
while num < 4:
    if count_hourglass(num) > result:
        result = count_hourglass(num)
    num += 1
print(result)
