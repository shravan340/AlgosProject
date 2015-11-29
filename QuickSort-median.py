# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 20:34:42 2015

@author: vineet
"""

import sys
import random

def quickSortMedian(numbers):
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
            temp=[numbers[1],numbers[0]]
            return temp
    else:
        if((size-1)!=0):
            num1, num2, num3 = random.sample(numbers, 3)
        if ((num1>num2) & (num1<num3)) | ((num1<num2) & (num1>num3)):
            pivot = num1
        elif ((num2>num1) & (num2<num3)) | ((num2<num1) & (num2>num3)):
            pivot = num2
        else:
            pivot = num3
        for i in range(0, size):
            if numbers[i] <= pivot:
                left.append(numbers[i])
            else:
                right.append(numbers[i])
    return quickSortMedian(left) + quickSortMedian(right)


content = [line.rstrip('\t') for line in open('2.txt')]
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
    ans = quickSortMedian(list)
    topk = ans[n-k:]
    with open("output.txt","w")as fp:
        fp.write("Using Quick Sort Median of three random element as pivot:\n")
        fp.write("%d th smallest element in array is %d\n"%(k, ans[k-1]))
        fp.write("%d top elements are:\n"%k)
        for line in reversed(topk):
            fp.write(str(line)+"\n")
        fp.write("Ascending order for the array is:\n")
        for line in ans:
            fp.write(str(line)+"\n")
