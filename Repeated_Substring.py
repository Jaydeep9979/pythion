import math,sys,os,collections,functools
if(os.path.exists('input.txt')):
	sys.stdin=open('input.txt','r')
	sys.stdout=open('output.txt','w')
for testcase in range(int(input())):
    s='abcabc'
    #abab
    print(s)
    print(s+s)
    print((s+s)[1:-1])