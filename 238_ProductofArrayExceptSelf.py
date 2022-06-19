

def solve(nums):

    result = []
    gunfol = 1
    gunfol2 = 1

    for i,v in enumerate(nums):
        if i>=0 and nums[i-1]== 0 and nums[i] ==0:
            gunfol=0
            print("in")

        if v == 0:
            gunfol2 = 0
            continue

        gunfol *= v

    print(gunfol)
    print(gunfol2)

    for i, v in enumerate(nums):

        if gunfol2 == 0:
            if v !=0:
                result.append(int(0))
            else:
                result.append(int(gunfol))
        else:
            result.append(int(gunfol / v))

    print(nums)
    print(result)




solve([[-1,1,0,-3,3]])