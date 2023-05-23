import sys
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def input_btree(s):
    file = open(fname, "r")
    inpbtree = file.readline()
    btree = inpbtree.split()
    for i in range(len(btree)):
        btree[i] = int(btree[i])
    file.close()
    return btree


def construct(lst):
    if not lst:
        return None
    
    value = lst.pop(0)
    if value == 0:
        return None
    
    node = TreeNode(value)
    node.left = construct(lst)
    node.right = construct(lst)
    
    return node

def transform(btree):
    global i
    l = []
    to_list_Inordertree(btree, l)
    sort(l)
    i = 0
    to_bin_search_tree(btree, l)

def printInorder(x):
    if x is not None:
        printInorder(x.left)
        print(x.value)
        printInorder(x.right)
        
def sort(ar):
    for i in range(1, len(ar)):
        key = ar[i]
        j = i - 1
        while (j >= 0 and ar[j] > key):
            ar[j+1] = ar[j]
            j = j - 1
        ar[j+1] = key
        
def to_list_Inordertree(x, r):
    if x is not None:
        to_list_Inordertree(x.left, r)
        r.append(x.value)
        to_list_Inordertree(x.right, r)

def copylist(array):
    copyar = []
    for i in range(len(array)):
        copyar.append(array[i])
    return copyar

def to_bin_search_tree(x, ar):
    global i
    if x is not None:
        to_bin_search_tree(x.left, ar)
        x.value = ar[i]
        i = i + 1
        to_bin_search_tree(x.right, ar)
        
def findPaths(btree, S):
    result = []
    findMonotonicPaths(btree, S, [], result)
    return result

def findMonotonicPaths(x, S, path, result):
    if x is None:
        return
    
    path.append(x.value)
    if to_sum(path) == S:
        result.append(list(path))
    if x.left is not None:
        findMonotonicPaths(x.left, S, path, result)
    if x.left is None and x.right is None:
        p = copylist(path)
        while len(p) > 1:
            p.pop(0)
            if to_sum(p) == S:
                result.append(list(p))
    if x.right is not None:
       findMonotonicPaths(x.right, S, path, result)
    path.pop(len(path) - 1)   

def to_sum(ar):
    s = 0
    for i in range(len(ar)):
        s = s + ar[i]
    return s

fname = sys.argv[1]
S = int(sys.argv[2])
out = 'ip_21_Horoshko_07_output_' + str(S) + '.txt'
inpbin_tree = input_btree(fname)
bin_tree = construct(inpbin_tree)
transform(bin_tree)
r = findPaths(bin_tree, S)
f = open(out, "w")
for i in range(len(r)):
    string = ' '.join(map(str, r[i])) + '\n'
    f.write(string)
f.close()


