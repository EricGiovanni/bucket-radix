import math


def insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b


def bucketSort(x):
    arr = []
    slot_num = len(x)
    m = max(x)
    for i in range(slot_num+1):
        arr.append([])

    print(arr)

    for j in x:
        index = math.floor(j*(slot_num/(m+1)))
        print("arr[", index, "].append(", j, ")")
        arr[index].append(j)
    print(arr)

    print("Ahora ordenamos cada bucket con insertion sort")
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])

    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    print("El arreglo ordenado es:")
    return x


x = [58398, 41751, 592, 52503, 8819, 22139, 43981,
     35925, 53561, 28063, 8284, 43301, 49486, 12704,
     49042, 30498, 40072, 54474, 18654, 45388, 11856,
     60230, 16744, 13729, 26251, 64056, 28912, 29924,
     38182, 61258, 3685, 47859, 61780, 1470, 21609,
     49915]
print(bucketSort(x))
