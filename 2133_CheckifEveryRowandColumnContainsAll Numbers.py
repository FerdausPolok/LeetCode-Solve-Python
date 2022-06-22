
def solve(matrix):
    result = True

    check = []
    check2 = []

    for i in matrix:
        for x in range(0, len(matrix[0])):
            check.append(x + 1)
        for j in i:

            if j not in check:
                result = False
                break
            else:
                check.remove(j)

    if result == False:

        print(result)
        return result

    else:
        for i, v in enumerate(matrix):
            for y in range(0, len(matrix[0])):
                check2.append(y + 1)

            for j, v2 in enumerate(v):
                value = matrix[j][i]
                if value not in check2:
                    result = False
                    break
                else:
                    check2.remove(value)

        print(result)
        return result


solve([[1,2,3],[3,2,1],[2,3,1]])