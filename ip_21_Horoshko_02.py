import sys
def SortandInv(arr):
    n = len(arr)
    temp = [0]*n
    return mergeSort(arr, temp, 0, n-1)
def mergeSort(arr, temp, left, right):
    inv = 0
    if left < right:
        mid = (left + right)//2
        inv += mergeSort(arr, temp, left, mid)
        inv += mergeSort(arr, temp, mid + 1, right)
        inv += merge(arr, temp, left, mid, right)
    return inv
def merge(arr, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left 
    inv = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            inv += mid - i + 1
            k += 1
            j += 1
    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1
    for el in range(left, right + 1):
        arr[el] = temp[el]
    return inv
def inputmatrix(lines, u, m):
    mat = []
    for row in lines:
        elements = row.split()
        mat.append(elements[1:])
    for i in range(u):
        for j in range(m):
            mat[i][j] = int(mat[i][j])
    return mat
def change(mat, num, u, m):
    for i in range(m):
        for j in range(m - i - 1):
            if(mat[num-1][j] > mat[num - 1][j+1]):
                changecol(mat, j, j+1, u)
def changecol(mat, fcol, scol, u):
    for i in range(u):
        el = mat[i][fcol]
        mat[i][fcol] = mat[i][scol]
        mat[i][scol] = el
def ins_sort(ar):
    for i in range(1, len(ar)):
        key = ar[i][1]
        k = ar[i]
        j = i - 1
        while (j >= 0 and ar[j][1] > key):
            ar[j+1] = ar[j]
            j = j - 1
        ar[j+1] = k
        
fname = sys.argv[1]
x = int(sys.argv[2])
file = open(fname, "r")
inpdim = file.readline()
dim = inpdim.split()
u = int(dim[0])
m = int(dim[1])
inpm = file.read()
rows = inpm.split("\n")
matrix = inputmatrix(rows, u, m)
change(matrix, x, u, m)
outm = []
for i in range(u):
    if(i != x -1):
        outm.append([i + 1, SortandInv(matrix[i])])
file.close()
ins_sort(outm)
out = 'ip_21_Horoshko_02_output' + '_' + str(u) + '_' + str(m) + '_' + str(x) +'.txt'
f = open(out, "w")
f.write('%d\n' %(x))
for i in range(u - 1):
    f.write("%d %d\n" %(outm[i][0], outm[i][1]))
f.close
