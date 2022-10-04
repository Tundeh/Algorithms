sampleArr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0],
             [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

sampleArr2 = [[-1, -1, 0, -9, -2, -2],

              [-2, -1, -6, -8, -2, -5],

              [-1, -1, -1, -2, -3, -4],

              [-1, -9, -2, -4, -4, -5],

              [-7, -3, -3, -2, -9, -9],

              [-1, -3, -1, -2, -4, -5]]
arr = [[-1, 1, -1, 0, 0, 0, ], [0, -1, 0, 0, 0, 0], [-1, -1, -1, 0, 0, 0, ],
       [0, -9, 2, -4, -4, 0], [-7, 0, 0, -2, 0, 0], [0, 0, -1, -2, -4, 0]]

sumArr = []
hourGlassArr = []
for x in range(0, len(arr)-2):
    subArr = arr[x]
    for i in range(0, len(subArr)-2):
        sum = subArr[i] + subArr[i+1] + subArr[i+2] + arr[x +
                                                          1][i + 1] + arr[x + 2][i] + arr[x+2][i+1] + arr[x+2][i+2]
        hourGlassArr.append([[subArr[i], subArr[i+1], subArr[i+2]],
                            [arr[x+1][i+1]], [arr[x + 2][i], arr[x+2][i+1], arr[x+2][i+2]]])
        sumArr.append(sum)

print("The max sum is", max(sumArr))
print(hourGlassArr)
