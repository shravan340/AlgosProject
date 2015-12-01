__author__ = 'Munna'
import sys
import random
list=[];
while len(list) <= 10000:
    num =random.randint(0, 10000)
    list.append(num)
with open ("Input_10K.txt","w")as fp:
        for line in list:
            fp.write(str(line)+"\n")
