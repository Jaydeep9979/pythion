import math,sys,os,collections,functools,itertools,string
if(os.path.exists('input.txt')):
	sys.stdin=open('input.txt','r')
	sys.stdout=open('output.txt','w')
for testcase in range(int(input())):
    s=input()
    stack=[]
    f=1
    for i in s:
        if i!=')':
            stack.append(i)
        else:
            if stack[-1]=='(':
                print("Duplicate parantheses")
                f=0
                break
            else:
                while stack[-1]!='(':
                    stack.pop()
                stack.pop()
    if f:
        print('No Duplicates')

