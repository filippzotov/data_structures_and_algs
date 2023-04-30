


def bubbleSort(input_array):
    
    sorting_array = input_array[:]
    return _bubbleSort(sorting_array)
    
    
def _bubbleSort(unsorted):
    
    for i in range(len(unsorted)):
        flag = True
        for j in range(len(unsorted)):
            
            if unsorted[j] > unsorted[i]:
                flag = False
                unsorted[i], unsorted[j] = unsorted[j], unsorted[i]
        if flag:
            break
    return unsorted


def selectionSort(input_array):
    sorting_array = input_array[:]
    return _selectionSort(sorting_array)


def _selectionSort(unsorted):
    
    for i in range(len(unsorted)):
        min_elem_index = i
        for j in range(i, len(unsorted)):
            if unsorted[j] < unsorted[min_elem_index]:
                min_elem_index = j
        if i != min_elem_index:
            unsorted[min_elem_index], unsorted[i] = unsorted[i], unsorted[min_elem_index]
    return unsorted
            
            
def insertionSort(input_array):
    sorting_array = input_array[:]
    return _insertionSort(sorting_array)

def _insertionSort(unsorted):
    
    for i in range(1, len(unsorted)):
        cur_item = unsorted[i]
        i -= 1
        while i >= 0 and cur_item < unsorted[i]:
            unsorted[i + 1] = unsorted[i]
            i -= 1
        unsorted[i + 1] = cur_item
            
    return unsorted


def quickSort(input_array):
    
    sorting_array = input_array[:]
    
    return _quickSort(sorting_array)

def _quickSort(unsorted):
    if len(unsorted) < 2:
        return unsorted
    mid = unsorted[0]
    swap_at = 0
    for i in range(len(unsorted) - 1):
        if unsorted[i + 1] < mid:
            unsorted[i + 1], unsorted[swap_at + 1] = unsorted[swap_at + 1], unsorted[i + 1]
            swap_at += 1
            
    unsorted[0], unsorted[swap_at] = unsorted[swap_at], unsorted[0]
    left = _quickSort(unsorted[:swap_at])
    right = _quickSort(unsorted[swap_at + 1:])
    left.append(unsorted[swap_at])
    return left + right