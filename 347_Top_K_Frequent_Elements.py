def topKFrequent(nums, k):

    dict={}
    for i, v in enumerate(nums):
        if v in dict:
            dict[v]= dict.get(v)+1
        else:
            dict[v]=1
    print(dict)
    dict2= {k: v for k, v in sorted(dict.items(), key= lambda v: v[1], reverse= True)}
    print(dict2)
    flag =0
    result = []
    for i, v in dict2.items():
        if flag == k:
            break
        else:
            result.append(i)
        flag +=1

    return result


print(topKFrequent([4,1,-1,2,-1,2,3], 2))



