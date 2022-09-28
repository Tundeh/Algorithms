# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    arrL = len(arr);
    rightDiff = 0;
    leftDiff = 0;
    for i in range(arrL):
        rightDiff += arr[i][i];
        leftDiff += arr[i][arrL - i - 1]
    diagDiff = rightDiff - leftDiff;
    return abs(diagDiff);