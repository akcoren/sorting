# O(n^2)
# Ex 
# [22,27,16,2,18,6]
# [16,22,27,2,18,6]
# [2,16,22,27,18,6]
# [2,16,18,22,27,6]
# [2,6,16,18,22,27]
#
#

def insertionSort(array):
    for i in range(1,len(array)):
        for j in range(i,0,-1):
            if array[j]<array[j-1]:
                temp = array[j]
                array[j]=array[j-1]
                array[j-1]=temp
            else:
                break
    return array
            

z = [5,2,6,8,9,4,1,7,3,8]
print(z)
a = insertionSort(z)
print(a)