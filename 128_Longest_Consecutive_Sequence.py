def solve(nums):
    check=set(nums)
    longest=0

    for i in nums:
        if (i-1) not in check:
            length = 0
            while (i+length) in check:
                length+=1
            longest= max(longest, length)
    return longest


print(solve([1,2,3,3,4,100,101]))