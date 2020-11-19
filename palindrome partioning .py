import math,sys,os,collections
if(os.path.exists('input.txt')):
	sys.stdin=open('input.txt','r')
	sys.stdout=open('output.txt','w')
for testcase in range(int(input())):
    s=input()
    pre={}
    arr=set()
    def solve(s,i,j):
        global arr
        def palindrome(arr,s,i,j):
            first=i
            last=j
            while first<last:
                if s[first]!=s[last]:
                    return False
                first+=1
                last-=1
           # print(s[i:j+1])
            arr.add(s[i:j+1])
            return True                
                
        if i>=j:
            return 0
        #print(palindrome(s,i,j))
        if palindrome(arr,s,i,j):
            
            return 0
        ans=float('inf')
        for k in range(i,j):
            if (i,k) in pre:
                t1=pre[(i,k)]
            else:
                t1=solve(s,i,k)
            if (k+1,j) in pre:
                t2=pre[(k+1,j)]
            else:
                t2=solve(s,k+1,j)
            temp=t1+t2+1
            ans=min(ans,temp)
        return ans
    
    print(solve(s,0,len(s)-1))
    print(arr)