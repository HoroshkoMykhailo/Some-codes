import sys
def copylist(array):
    copyar = []
    for i in range(len(array)):
        copyar.append(array[i])
    return copyar

def Quicksort1(A, p, r):
    if p<r:
        q = partition1(A, p, r, 1)
        Quicksort1(A, p, q-1)
        Quicksort1(A, q+1, r)
        
def partition2(A, p, r):
    if(A[p] > A[(p + r)//2 + 1] and A[(p+r)//2 + 1] < A[r]):
        if(A[p] > A[r]):
            pivot = r
        else:
            pivot = p
    elif(A[p] > A[r] and A[(p+r)//2 + 1] > A[r]):
        if(A[p] > A[(p+r)//2 + 1]):
            pivot = (p + r)//2 + 1
        else:
            pivot = p
    else:
        if(A[r] > A[(p+r)//2 + 1]):
            pivot = (p+r)//2 + 1
        else:
            pivot = r
    if(pivot != r):
        el = A[r]
        A[r] = A[pivot]
        A[pivot] = el
    return partition1(A, p, r, 2)

def partition1(A, p, r, c):
    global n1
    global n2
    x = A[r]
    pivot = r
    i = p - 1
    for j in range(p, r):
        if(c == 1):
            n1 = n1 + 1
        else:
            n2 = n2 + 1
        if(A[j]<=x):
            i = i + 1
            el = A[i]
            A[i] = A[j]
            A[j] = el
    el = A[i+1]
    A[i+1] = A[pivot]
    A[pivot] = el
    return i + 1

def Quicksort2(A, p, r):
    if p<r:
        if((r - p) <= 3):
            insertion_sort(A, p, r, 2)
        else:
            q = partition2(A, p, r)
            Quicksort2(A, p, q-1)
            Quicksort2(A, q+1, r)
            
def insertion_sort(A, p, r, c):
    global n2
    global n3
    for i in range(p + 1, r +1):
        key = A[i]
        j = i - 1
        if(c == 2):
            n2 = n2 + 1
        else:
            n3 = n3 + 1
        while (j >= p and A[j] > key):
            A[j+1] = A[j]
            j = j - 1
            if(c == 2):
                n2 = n2 + 1
            else:
                n3 = n3 + 1
        A[j+1] = key
def Quicksort3(A, p, r):
    if p<r:
        if((r - p) <= 3):
            insertion_sort(A, p, r, 3)
        else:
            if(A[p] > A[p+1] and A[p+1] < A[r]):
                if(A[p] > A[r]):
                    el = A[p + 1]
                    A[p + 1] = A[p]
                    A[p] = el
                    el = A[p + 1]
                    A[p + 1] = A[r]
                    A[r] = el
                else:
                    el = A[p + 1]
                    A[p + 1] = A[p]
                    A[p] = el
            elif(A[p] > A[r] and A[p+1] > A[r]):
                if(A[p] > A[p+1]):
                    el = A[p]
                    A[p] = A[r]
                    A[r] = el
                else:
                    el = A[p + 1]
                    A[p + 1] = A[r]
                    A[r] = el
                    el = A[p + 1]
                    A[p + 1] = A[p]
                    A[p] = el
            else:
                if(A[r] < A[p + 1]):
                    el = A[p + 1]
                    A[p + 1] = A[r]
                    A[r] = el
            q = partition3(A, p, r)
            Quicksort3(A, p, q[0]-1)
            Quicksort3(A, q[0]+1, q[1]-1)
            Quicksort3(A, q[1]+1, q[2]-1)
            Quicksort3(A, q[2]+1, r)
def partition3(A, p, r):
    global n3
    a = p + 2
    b = p + 2
    c = r - 1
    d = r - 1
    q1 = A[p]
    q2 = A[p+1]
    q3 = A[r]
    while(b <= c):
        n3 = n3 + 1
        while(A[b] < q2 and b <=c):
            n3 = n3 + 1
            if(A[b] < q1):
                el = A[a]
                A[a] = A[b]
                A[b] = el
                a = a + 1
            b = b + 1
            n3 = n3 + 1
        n3 = n3 + 1
        while(A[c] > q2 and b <=c):
            n3 = n3 + 1
            if(A[c]>q3):
                el = A[c]
                A[c] = A[d]
                A[d] = el
                d = d - 1
            n3 = n3 + 1
            c = c - 1
        if(b<=c):
            n3 = n3 + 1
            if(A[b] > q3):
                n3 = n3 + 1
                if(A[c] < q1):
                    el = A[a]
                    A[a] = A[b]
                    A[b] = el
                    el = A[a]
                    A[a] = A[c]
                    A[c] = el
                    a = a + 1
                else:
                    el = A[b]
                    A[b] = A[c]
                    A[c] = el
                el = A[c]
                A[c] = A[d]
                A[d] = el
                b = b + 1
                c = c - 1
                d = d - 1
            else:
                n3 = n3 + 1
                if(A[c] < q1):
                    el = A[a]
                    A[a] = A[b]
                    A[b] = el
                    el = A[a]
                    A[a] = A[c]
                    A[c] = el
                    a = a + 1
                else:
                    el = A[b]
                    A[b] = A[c]
                    A[c] = el
                b = b + 1
                c = c - 1
    a = a - 1
    b = b - 1
    c = c + 1
    d = d + 1
    el = A[p+1]
    A[p+1] = A[a]
    A[a] = el
    el = A[a]
    A[a] = A[b]
    A[b] = el
    a = a - 1
    el = A[p]
    A[p] = A[a]
    A[a] = el
    el = A[r]
    A[r] = A[d]
    A[d] = el
    q = [a, b, d]
    return q
fname = sys.argv[1]
file = open(fname, "r")
N = int(file.readline())
ar = [0]*N
for i in range(N):
    ar[i] = int(file.readline())
n1 = 0
n2 = 0
n3 = 0
arr = copylist(ar)
Quicksort1(arr, 0, N - 1)
array = copylist(ar)
Quicksort2(array, 0, N - 1)
Quicksort3(ar, 0, N - 1)
file.close()
out = 'ip_21_Horoshko_02_output_' + str(N) + '.txt'
f = open(out, "w")
f.write('%d %d %d' %(n1, n2, n3))
f.close()


