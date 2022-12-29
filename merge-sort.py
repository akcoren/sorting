# Merge Sort algorithm
# O(n*log(n))
# Example case:
# [16,21,11,8,12,22]
# [16,21,11] [8,12,22]
# [16] [21,11] [8] [12,22] 
# [16] [21] [11] [8] [12] [22]
# [16] [11,21] [8] [12,22]
# [11,16,21] [8,12,22]
# [8,11,12,16,21,22]
# 

def mergeSort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2 

    A = array[:mid]
    B = array[mid:]

    sortedA = mergeSort(A)
    sortedB = mergeSort(B)

    return merge(sortedA,sortedB)
    # return merge(mergeSort(A),mergeSort(B))



def merge(arrayA, arrayB):

    k = 0   
    i = 0
    j = 0
    temp = []
    while (i<len(arrayA) and j<len(arrayB)):

        if(arrayA[i]<=arrayB[j]):
            temp.append(arrayA[i])
            k = k + 1
            i = i + 1

        else:
            temp.append(arrayB[j])
            k = k + 1
            j = j + 1

    while (i<len(arrayA)):
        temp.append(arrayA[i])
        k = k + 1
        i = i + 1

    while (j<len(arrayB)):
        temp.append(arrayB[j])
        k = k + 1
        j = j + 1

    return temp


feed = [16,21,11,8,12,22]
result = mergeSort(feed)
print(result)