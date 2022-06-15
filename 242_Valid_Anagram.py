def solve(str1, str2):

    str3= sorted(str1)
    str4= sorted(str2)


    if str3 == str4:
        return True
    else:
        return  False

print(solve("rat", "car"))
