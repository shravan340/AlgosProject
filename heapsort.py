
import sys
import time
def Max_Heapify(array, i):
    l = 2*i+1
    r = 2*i+2
    if l < heap_size and array[l] > array[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and array[r] > array[largest]:
        largest = r
    if largest != i:
        temp = array[i]
        array[i] = array[largest]
        array[largest] = temp
        Max_Heapify(array, largest)

def Build_Heap(array):
    global heap_size
    heap_size = len(array)
    for j in range(int(len(array)/2), -1, -1):
        Max_Heapify(array, j)

def Heap_Sort(array):
    Build_Heap(array)
    global heap_size
    for i in range(len(array)-1, -1, -1):
        temp = array[0]
        array[0] = array[i]
        array[i] = temp
        heap_size -= 1
        Max_Heapify(array, 0)

def Return_Max(array):
    Max_Heapify(array, 0)
    return array[0]

#a = [2, 7, 3, 9, 1, 4, 8, 6, 5, 0]
heap_size = None
content = [line.rstrip('\t') for line in open('input.txt')]
k,n=content[0].split()
k=int(k)
n=int(n)
if n==0 :
    print("The List is empty and no elements to display")
    sys.exit
else:
    list= []
    ans=[]
    j=0
    for i in content:
        if j==0:
            j+=1
            continue
        i=i.strip()
        i=int(i)
        list.append(i)
    t1=time.time()
    Heap_Sort(list)
    t2=time.time()
    print (t2-t1)
    topk= list[n-k:]
    with open ("Output_HeapSort.txt","w")as fp:
        fp.write("the %d th smallest element in array is %d\n"%(k, list[k-1]))
        fp.write("the %d top elements are:\n"%k)
        for line in reversed(topk):
            fp.write(str(line)+"\n")
        fp.write("the ascending order for the array is:\n")
        for line in list:
            fp.write(str(line)+"\n")
print ("done")

