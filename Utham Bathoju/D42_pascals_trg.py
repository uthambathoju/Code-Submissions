def pascals_triag(numRows):
    res=[[1]]
    for i in range(numRows-1):
        arr = res[-1]
        arr = [0] + arr + [0]
        temp = []
        for j in range(0, len(arr)-1):
            temp.append(arr[j] + arr[j + 1])
        res.append(temp)
