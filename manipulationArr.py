def arrayManipulation(n, queries):
    # Write your code here
    arr = []
    for i in range(0, n):
        arr.append(0)
    for x in range(0, len(queries)):
        for z in range(queries[x][0] - 1, queries[x][1]):
            print(z)
            arr[z] = arr[z] + queries[x][2]
        print(arr)
    return max(arr)


narr = [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]
print(arrayManipulation(10, narr))
