# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 21:02:16 2015

@author: vineet
"""

import random
import sys
import time

def getPivotIndex(start, end):
    num1 = random.randint(start, end)
    num2 = random.randint(start, end)
    num3 = random.randint(start, end)
    if ((list[num1]>list[num2]) & (list[num1]<list[num3])) | ((list[num1]<list[num2]) & (list[num1]>list[num3])):
            pivot = num1
    elif ((list[num2]>list[num1]) & (list[num2]<list[num3])) | ((list[num2]<list[num1]) & (list[num2]>list[num3])):
        pivot = num2
    else:
        pivot = num3
    return pivot


def Quicksort(start, end):
    if start < end:
        pivotIndex = partition(start, end, getPivotIndex(start, end))
        Quicksort(start, pivotIndex - 1)
        Quicksort(pivotIndex + 1, end)

def partition(start, end, pivotIndex):
    pivotIndexAfterPartition = start
    pivot = list[pivotIndex]
    swap(pivotIndex, end)
    for i in range(start, end, 1):
        if list[i] <= pivot:
            swap(i, pivotIndexAfterPartition)
            pivotIndexAfterPartition += 1
    swap(end, pivotIndexAfterPartition)
    return pivotIndexAfterPartition


def swap(i, j):
    temp = list[i]
    list[i] = list [j]
    list[j] = temp


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
    start = 0
    end = len(list) - 1
    t1=time.time()
    Quicksort(start, end)
    t2=time.time()
    print(t2-t1)    
    topk= list[n-k:]
    with open ("output_QuickSort_with_Insertionsort.txt","w")as fp:
        fp.write("the %d th smallest element in array is %d\n"%(k, list[k-1]))
        fp.write("the %d top elements are:\n"%k)
        for line in reversed(topk):
            fp.write(str(line)+"\n")
        fp.write("the ascending order for the array is:\n")
        for line in list:
            fp.write(str(line)+"\n")
