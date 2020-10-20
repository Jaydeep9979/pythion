import math,sys,os,collections
if(os.path.exists('input.txt')):
	sys.stdin=open('input.txt','r')
	sys.stdout=open('output.txt','w')
for testcase in range(int(input())):
    arr=[5, 6, 7, 8, 9]
    m=5
    pre=collections.defaultdict(int)
    pre[0]=1
    count=0
    curr=0
    max_xor=0
    for i,num in enumerate(arr):
        curr^=num
        if curr^m in pre:
            count+=pre[curr^m]
        pre[curr]+=1
    print(count)
