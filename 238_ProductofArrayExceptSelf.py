def solve(nums,):

    result = []
    pre = []
    post= [""] * len(nums)

    f=1
    l=1
    length = len(nums)
    for i,v in enumerate(nums):
        f *= v
        pre.append(f)
        l *= nums[length-1]
        post[length-1] = l
        length-=1
    print("pre: ",pre)
    print("post: ",post)

    for i,v in enumerate(nums):

         if i ==0:
             result.append(post[1])
         elif i == len(nums)-1:
             result.append(pre[len(nums)-2])
         else:
             result.append(pre[i-1] * post[i+1])


    return result







solve([1,2,3,4])