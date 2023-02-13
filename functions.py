import time
def copylist(array):
    copyar = []
    for i in range(len(array)):
        copyar.append(array[i])
    return copyar
def bubble_sort(arr, r):
    if r != 1:
        ar = copylist(arr)
    else:
        ar = arr
    k = 0
    t = 0
    n = len(ar)
    start = time.time()
    for i in range(n-1):
        for j in range(n-i-1):
            k = k + 1
            if ar[j] > ar[j+1]:
                el = ar[j]
                ar[j]=ar[j+1]
                ar[j+1] = el
                t = t + 1
    end = time.time()
    if r == 1:
        print('Number of comparition: %d Number of swapping: %d' %(k, t))
    return (end - start)
def mod_bubble_sort(arr, r):
    if r != 1:
        ar = copylist(arr)
    else:
        ar = arr
    k = 0
    t = 0
    n = len(ar)
    start = time.time()
    for i in range(n-1):
        swap = False
        for j in range(n-i-1):
            k = k + 1
            if ar[j] > ar[j+1]:
                el = ar[j]
                ar[j]=ar[j+1]
                ar[j+1] = el
                swap = True
                t = t + 1
        if not swap:
            break
    end = time.time()
    if r == 1:
        print('Number of comparition: %d Number of swapping: %d' %(k, t))
    return (end - start)
def insertion_sort(arr, r):
    if r != 1:
        ar = copylist(arr)
    else:
        ar = arr
    k = 0
    t = 0
    start = time.time()
    for i in range(1, len(ar)):
        key = ar[i]
        j = i - 1
        k = k + 1
        while (j >= 0 and ar[j] > key):
            ar[j+1] = ar[j]
            j = j - 1
            k = k + 1
            t = t + 1
        ar[j+1] = key
    end = time.time()
    if r == 1:
        print('Number of comparition: %d Number of swapping: %d' %(k, t))
    return(end - start)
