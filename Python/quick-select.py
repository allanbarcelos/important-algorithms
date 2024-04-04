def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSelect(arr, k):
    def helper(arr, low, high, k):
        if low <= high:
            pivot_index = partition(arr, low, high)
            if pivot_index == k:
                return arr[pivot_index]
            elif pivot_index < k:
                return helper(arr, pivot_index + 1, high, k)
            else:
                return helper(arr, low, pivot_index - 1, k)
    
    return helper(arr, 0, len(arr) - 1, k - 1)

# Teste unitário
def test_quickSelect():
    arr = [3, 2, 1, 5, 6, 4]
    assert quickSelect(arr, 2) == 2

test_quickSelect()
