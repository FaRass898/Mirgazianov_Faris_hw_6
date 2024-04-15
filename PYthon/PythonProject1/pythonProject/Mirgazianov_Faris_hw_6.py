def bubble_sort(num):
    for i in range(len(num)):
        for j in range(len(num) - i - 1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]


numbers = [2, 4, 6, 8, 3, 9, 1, 5]
sorted_list = bubble_sort(numbers)


print(numbers)


def  binary_search (arr, val):
    first = 0
    last = len(arr)-1
    while first < last:
        middle = (first + last) // 2
        if val == arr[middle]:
            first = middle
            last = middle
            print(f'Элемент {val} найден в позиции {middle}')
            return middle
        elif val > arr[middle]:
            first = middle + 1
        else:
            last = middle - 1

    print(f'Элемент не найден')


fol = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, ]
find = 10
binary = binary_search(fol, find)