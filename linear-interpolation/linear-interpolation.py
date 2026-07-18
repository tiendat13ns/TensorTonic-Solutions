def linear_interpolation(values):
    """
    Fill missing (None) values using linear interpolation.
    """
    # Write code here
    result = values[:]
    n = len(result)

    i = 0
    while i < n:
        if result[i] is None:
            left = i - 1

            right = i
            while result[right] is None:
                right += 1

            left_value = result[left]
            right_value = result[right]
            gap = right - left

            for j in range(left + 1, right):
                ratio = (j - left) / gap
                result[j] = left_value + ratio * (right_value - left_value)

            i = right
        else:
            i += 1

    return result