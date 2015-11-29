import random

__author__ = 'Munna'

import sys
def quickSortUsingRandomPivot(numbers):
    left = []
    right = []
    size = len(numbers)
    if size == 0:
        return numbers
    elif size == 1:
        return numbers
    elif size == 2:
        if (numbers[1] > numbers[0]):
            return numbers
        else:
            return reversed(numbers)
    else:
        if((size-1)!=0):
            num = random.randint(0, size-1)
        pivot = numbers[num]
        for i in range(0, size):
            if numbers[i] <= pivot:
                left.append(numbers[i])
            else:
                right.append(numbers[i])
    return quickSortUsingRandomPivot(left) + quickSortUsingRandomPivot(right)


content = [line.rstrip('\t') for line in open('1.txt')]
k,n=content[0].split()
k=int(k)
n=int(n)
if n==0:
    print("List is empty and no elements to display")
    sys.exit
else:
    list = []
    ans=[]
    j=0
    for i in content:
        if j == 0:
            j += 1
            continue
        i=i.strip()
        i=int(i)
        list.append(i)
    ans = quickSortUsingRandomPivot(list)
    topk = ans[n-k:]
    with open("output.txt","w")as fp:
        fp.write("Using Quick Sort Random Element as pivot:\n")
        fp.write("%d th smallest element in array is %d\n"%(k, ans[k-1]))
        fp.write("%d top elements are:\n"%k)
        for line in reversed(topk):
            fp.write(str(line)+"\n")
        fp.write("Ascending order for the array is:\n")
        for line in ans:
            fp.write(str(line)+"\n")
