# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 18:45:55 2015

@author: vineet
"""
import sys
def quickSort(numbers):
    left = []
    right = []
    size = len(numbers)
    if size == 1:
        return numbers
    elif size == 2:
        if(numbers[1]<numbers[0]):
            return list([numbers[1],numbers[0]])
        else:
            return numbers
    else:
        key = numbers[0]
        for i in range(1,size):
            if numbers[i]<key:
                left.append(numbers[i])
            else:
                right.append(numbers[i])
        left.append(key)
    return quickSort(left) + quickSort(right)

content = [line.rstrip('\t') for line in open('1.txt')]
k,n=content[0].split()

if n=='0' :
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
    ans= quickSort(list)  
    print(ans)
    with open ("output.txt","w")as fp:
        for line in ans:
            fp.write(str(line)+"\n")


  