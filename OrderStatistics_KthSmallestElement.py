__author__ = 'Munna'
import sys
import time
def findMedian(arr):
    arr.sort()
    return arr[len(arr)//2]

def kthsmallest(arr,l,r,k):
    if k > 0 and k <= r-l +1:
        n=r-l+1
        median=[0 for x in range((n+4)//5)]
<<<<<<< HEAD
        temp=(n//5)
=======
        #number=[]
        #num=[]
        temp=int(n/5)
>>>>>>> origin/master
        i=0
        for i in range (temp):
            start=l+i*5
            median[i]=findMedian(arr[start:start+5])
            i=i+1
        if i*5<n:
            start=l+i*5
            median[i]=findMedian(arr[start:start+5])
            i=i+1
        if i==1:
            medOfMed = median[i-1]
        else:
            medOfMed = kthsmallest(median,0,i-1,i//2)
        pos= partition(arr,l,r,medOfMed)
        if pos-l == k-1:
            return arr[pos]
        if pos-l>k-1:
            return kthsmallest(arr,l,pos-1,k)
        return kthsmallest(arr,pos+1,r,k-pos+l-1)
    return pow(2,31)

def partition(arr,l,r,x):
    i=l
    for i in range(r):
        if arr[i]==x:
            break
        i=i+1
    swap(arr,i,r)
    i=l
    for j in range(r):
        if arr[j]<=x:
            swap(arr,i,j)
            i+=1
    swap(arr,i,r)
    return i

def swap(arr,i,r):
    arr[i], arr[r] = arr[r], arr[i]

content = [line.rstrip('\t') for line in open('Input.txt')]
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
    ksmall =kthsmallest(list,start,end,k)
    print(ksmall)
    t2=time.time()
    print (t2-t1)
    with open ("Output_OrderStatistics.txt","w")as fp:
        fp.write("The %dth smallest element: %d"%(k, list[k-1]))