def binarySearch(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Teste unitário
def test_binarySearch():
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    assert binarySearch(arr, target) == 3

test_binarySearch()
