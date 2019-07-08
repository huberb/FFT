# Fast Fourier Transform in O(n log n) using Divide and Conquer

import math

def fast_fourier_transform(nums):
    n = len(nums)

    if n == 1: return nums

    left_side = [num for index, num in enumerate(nums) if index % 2 == 0]
    right_side = [num for index, num in enumerate(nums) if index % 2 == 1]

    transformed_left = fast_fourier_transform(left_side)
    transformed_right = fast_fourier_transform(right_side)

    inverted_root = math.e ** (2 * math.pi * 1j / n)
    root = 1

    res = [0] * n
    for index in range(0, int(n/2)):
        res[index] = transformed_left[index] + root * transformed_right[index]
        res[int(index + n/2)] = transformed_left[index] - root * transformed_right[index]
        root = root * inverted_root
    return res

test = [0, 18, -15, 3]
print(fast_fourier_transform(test))
