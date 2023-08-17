# o(n2)
def detectPair(values,totalSum):
    for i in range(0,len(values) - 1):
        for j in range(i+1, len(values)):
            if(values[i] + values[j]  == totalSum):
                return [values[i],values[j]]

    return []

# o(nlogn)
def detectPairV2(values, totalSum):
    values = sorted(values)
    print(f'sorted is {values}')
    firstIndex,lastIndex = 0, len(values) -1

    while values[firstIndex] < values[lastIndex]:
        if(values[firstIndex]+values[lastIndex] > totalSum):
            lastIndex -= 1
        elif(values[firstIndex]+values[lastIndex] < totalSum):
            firstIndex += 1
        else:
            return [values[firstIndex],values[lastIndex]]
    return []

# o(n)
def detectPairV3(values,totalSum):
    seen_value=[] #1,2,4,
    for value in values: #1,2,4,8
        complete = totalSum - value #12 - 8 = 4
        if complete in seen_value:
            return [value,complete]
        else:
            seen_value.append(value)

    return []


# print(detectPair([-1,-2,12,3,4], 10))
# print(detectPairV2([1,-2,-10,4, 10],14 ))
print(detectPairV3([1,-2,-4,8],-6))
