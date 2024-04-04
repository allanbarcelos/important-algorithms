def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Teste unitário
def test_insertionSort():
    arr = [12, 11, 13, 5, 6]
    insertionSort(arr)
    assert arr == [5, 6, 11, 12, 13]

test_insertionSort()
