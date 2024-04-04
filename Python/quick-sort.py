def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quickSort(less_than_pivot) + [pivot] + quickSort(greater_than_pivot)

# Teste unitário
def test_quickSort():
    arr = [10, 7, 8, 9, 1, 5]
    assert quickSort(arr) == [1, 5, 7, 8, 9, 10]

test_quickSort()
