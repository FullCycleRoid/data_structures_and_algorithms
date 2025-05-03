def merge_sort(unsorted: list) -> list:
    if len(unsorted) == 1:
        return unsorted

    pivot = int(len(unsorted) / 2)

    left_arr = merge_sort(unsorted[:pivot])
    right_arr = merge_sort(unsorted[pivot:])
    return merge_arrays(left_arr, right_arr)


def merge_arrays(left: list, right: list) -> list:
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result.extend(left)
    result.extend(right)

    return result


list1 = [5,2,6,8,0,33,547,2,2,6]
list2 = [2,54,765,2,4,8,0,87,56,34]

list3 = list1 + list2
result = merge_sort(list3)
print(result)
a = 0