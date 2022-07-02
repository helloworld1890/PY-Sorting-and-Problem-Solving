# Write your solution for algorithm 4 below
str_1 =  'I love software engineering'

def merge_sorted(lst):
    if lst <= 1:
        return lst
    else:
        middle_index = len(lst) // 2
        left = lst[:middle_index]
        right = lst[middle_index:]
        left_partition = merge_sort(left)
        right_partition = merge_sort(right)
        return merge(left_partition, right_partition)

def merge(lst1, lst2):
    results = []
    while lst1 and lst2:
        if lst1[0] < lst2[0]:
            results.append(lst1.pop(0))
        else:
            results.append(lst2.pop(0))
    
    return results + lst1 + lst2

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    # Split the list
    length = len(arr)
    mid = length // 2
    
    left = arr[:mid]
    right = arr[mid:]
    
    print(f'left --> {left}')
    print(f'right --> {right}')
      
    return merge(merge_sort(left), merge_sort(right))

# def merge(left, right):
#     result = []
#     left_index = 0
#     right_index = 0
    
#     while left_index < len(left) and right_index < len(right):
#         if left[left_index] < right[right_index]:
#             result.append(left[left_index])
#             left_index += 1
#         else:
#             result.append(right[right_index])
#             right_index += 1

#     result += left[left_index:]
#     result += right[right_index:]
    
#     return result