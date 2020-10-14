import math,sys,os,collections
if(os.path.exists('input.txt')):
	sys.stdin=open('input.txt','r')
	sys.stdout=open('output.txt','w')
for testcase in range(int(input())):
    arr=list(map(int,input().split()))
    n=len(arr)
    i=0
    j=0
    dic=collections.defaultdict(int)
    ans=0
    k=len(set(arr))
    while True:
        f1,f2=False,False
        while i<n:
            f1=True
            dic[arr[i]]+=1
            if len(dic)==k:
                ans+=(n-i)
                break
            i+=1
        #print(dic)
        while j<i:
            print(i,j)
            f2=True
            dic[arr[j]]-=1
            if dic[arr[j]]==0:
                del dic[arr[j]]
            
            if len(dic)==k:
                ans+=(n-i)
            else:
                j+=1
                break
            j+=1
        if not f1 and not f2:
            break
    print(ans)
        



        
            
            