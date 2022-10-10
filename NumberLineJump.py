def kangaroo(x1, v1, x2, v2):
    # Write your code here

    if (v2 > v1):
        return "NO"

    z = v1 - v2
    y = x2 - x1

    if (z > 0 and y > 0):
        result = y/z
        print(result % 1)
        if (result % 1 == 0):
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


print(kangaroo(43, 2, 70, 2))
