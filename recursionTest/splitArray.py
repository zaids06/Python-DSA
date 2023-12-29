def splitArray(input):
    return splitArrayHelper(input, 0, 0, 0)


def splitArrayHelper(arr, si, lsum, rsum):
    if si == len(arr):
        return lsum == rsum

    if arr[si] % 5 == 0:
        lsum += arr[si]
    elif arr[si] % 3 == 0:
        rsum += arr[si]
    else:
        return splitArrayHelper(arr, si + 1, lsum + arr[si], rsum) or splitArrayHelper(arr, si + 1, lsum,
                                                                                       rsum + arr[si])

    return splitArrayHelper(arr, si + 1, lsum, rsum)


# Example usage:
arr = [30, 20, 53, 14]
result = splitArray(arr)
print(result)
