
def binary_search(num, target):
    lo= 0
    hi= len(num)-1


    while lo <= hi:
        mid = (lo + hi) // 2

        if num[mid] == target:
            return mid
        elif num[mid] > target:
            hi= mid-1
        elif num[mid] < target:
            lo = mid+1

#print(binary_search([1,2,3,4,5,6], 4))

def selectionSort(nums):

    for i in range (0, len(nums)):
        min_value_index = i
        for j in range (i+1, len(nums)):
            if(nums[j] < nums[min_value_index]):
                min_value_index = j
        if min_value_index != i:
            nums[min_value_index], nums[i] = nums[i], nums[min_value_index]

    print(nums)

#selectionSort([10,-1,85,12,7,3,8,1,4,3,5])

def fibo(n):
    if n<= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)


print(fibo(5))


def fibo2(n):
    if n <= 0:
        return "Incorrect input"
    elif n ==1:
        print(0)
    elif n==2:
        print(0, 1)
    else:
        res=[0,1]
        x = n
        a = 0
        b = 1
        while x>2:

            c =a+b
            res.append(c)
            a=b
            b=c
            x-=1
        print(res)