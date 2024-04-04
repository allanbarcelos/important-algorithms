def countingSort(arr):
    max_val = max(arr)
    counts = [0] * (max_val + 1)

    for num in arr:
        counts[num] += 1

    output = []
    for i in range(len(counts)):
        output.extend([i] * counts[i])

    return output

# Teste unitário
def test_countingSort():
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert countingSort(arr) == [1, 2, 2, 3, 3, 4, 8]

test_countingSort()
