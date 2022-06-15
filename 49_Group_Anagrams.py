def groupAnagrams(strs):

    hmap= {}

    for i in strs:
        temp = "".join(sorted(i))

        if temp in hmap:
            hmap[temp].append(i)
        else:
            hmap[temp]= [i]

    result = []

    for i, v in hmap.items():
        result.append(v)

    return result

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))