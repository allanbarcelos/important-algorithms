def maxSlidingWindow(nums, k):
    if not nums:
        return []

    result = []
    window = []

    for i, num in enumerate(nums):
        if window and window[0] <= i - k:
            window.pop(0)

        while window and nums[window[-1]] <= num:
            window.pop()

        window.append(i)

        if i >= k - 1:
            result.append(nums[window[0]])

    return result

# Teste unitário
def test_maxSlidingWindow():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    assert maxSlidingWindow(nums, k) == [3, 3, 5, 5, 6, 7]

test_maxSlidingWindow()
