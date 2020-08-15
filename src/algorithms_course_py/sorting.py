def bubblesort(dataset):
    for i in range(len(dataset) - 1, 0, -1):
        for j in range(i):
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp
    return dataset


def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        left_arr = dataset[:mid]
        right_arr = dataset[mid:]

        mergesort(left_arr)
        mergesort(right_arr)
        
        i = 0
        j = 0
        k = 0
        
        # merge while both arrays have values
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] > right_arr[j]:
                dataset[k] = right_arr[j]
                j += 1
            else:
                dataset[k] = left_arr[i]
                i += 1
            k += 1
        
        # merge remaining
        while i < len(left_arr):
            dataset[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            dataset[k] = right_arr[j]
            j += 1
            k += 1
    

def quicksort(dataset, first, last):
    if first < last:
        # find split point
        i_pivot = partition(dataset, first, last)
        
        # sort partitions
        quicksort(dataset, first, i_pivot - 1)
        quicksort(dataset, i_pivot + 1, last)

def partition(dataset, first, last):
    pivot = dataset[first]
    
    lower = first + 1
    upper = last
    
    done = False
    while not done:
        while lower <= upper and dataset[lower] <= pivot:
            lower += 1
        while upper >= lower and dataset[upper] >= pivot:
            upper -= 1
        
        if upper < lower:
            # found crossing point
            done = True
        else:
            temp = dataset[lower]
            dataset[lower] = dataset[upper]
            dataset[upper] = temp

    # exchange pivot point
    temp = dataset[first]
    dataset[first] = dataset[upper]
    dataset[upper] = temp
    
    return upper


data1 = [345, 76, 2, 65, 87, 76, 78, 12, 43]

run_data = list(data1)
print("Bubble sort:")
print(run_data)
bubblesort(run_data)
print(run_data)

run_data = list(data1)
print("Merge sort:")
print(run_data)
mergesort(run_data)
print(run_data)

run_data = list(data1)
print("Quick sort:")
print(run_data)
quicksort(run_data, 0, len(run_data) - 1)
print(run_data)