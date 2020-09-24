import math,sys,os,collections
if(os.path.exists('input.txt')):
	sys.stdin=open('input.txt','r')
	sys.stdout=open('output.txt','w')
s=input()
seen={}
l=0
ans=0
arr=[1,2,3]
print(arr[0:0])
for i in range(len(s)):
	if s[i] in seen and seen[s[i]]>=l:
		l=seen[s[i]]+1
	else:
		ans=max(ans,i-l+1)
	seen[s[i]]=i
print(ans)

