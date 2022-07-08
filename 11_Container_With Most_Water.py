def solve(height):
    lo = 0
    hi = len(height) - 1
    res = 0

    while lo < hi:
        area = (hi - lo) * min(height[lo], height[hi])
        res = max(res, area)

        if height[lo] > height[hi]:
            hi -= 1
        else:
            lo += 1

    return res

    return max

print(solve([1,8,6,2,5,4,8,3,7]))