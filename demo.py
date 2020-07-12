import math,bisect,heapq,collections,itertools,datetime,functools,sys,os
if os.path.exists("input.txt"):
    sys.stdout=open("output.txt","w")
    sys.stdin=open("input.txt","r") 

for testcase in range(int(input())):
    arr=[1 for i in range(n)]
    print(*arr)