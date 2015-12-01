# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 18:45:55 2015

@author: vineet
"""
import sys
import time
def quickSort(numbers):
    left = []
    right = []
    size = len(numbers)
    if size == 1:
        return numbers
    elif size == 2:
        if(numbers[1]>numbers[0]):
            return numbers
        else:
            temp=[numbers[1],numbers[0]]
            return temp
    else:
        key = numbers[0]
        for i in range(1,size):
            if numbers[i]<key:
                left.append(numbers[i])
            else:
                right.append(numbers[i])
        left.append(key)
    return quickSort(left) + quickSort(right)

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
    ans= quickSort(list)  
    t2=time.time()
    print (t2-t1)
    topk= ans[n-k:]
    with open ("Output_QuickSort_FirstElement.txt","w")as fp:
        fp.write("the %d th smallest element in array is %d\n"%(k, ans[k-1]))
        fp.write("the %d top elements are:\n"%k)
        for line in reversed(topk):
            fp.write(str(line)+"\n")    
        fp.write("the ascending order for the array is:\n")
        for line in ans:
            fp.write(str(line)+"\n")