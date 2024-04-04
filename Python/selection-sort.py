def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Teste unitário
def test_selectionSort():
    arr = [64, 25, 12, 22, 11]
    selectionSort(arr)
    assert arr == [11, 12, 22, 25, 64]

test_selectionSort()
