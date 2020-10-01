import math,sys,os,collections
if(os.path.exists('input.txt')):
	sys.stdin=open('input.txt','r')
	sys.stdout=open('output.txt','w')
for testcase in range(int(input())):
	arr=list(map(int,input().split()))
	low=0;mid=0;high=len(arr)-1
	while mid<=high:
		if arr[mid]>1:
			print(f'first {arr[mid],arr[high]}')
			arr[mid],arr[high]=arr[high],arr[mid]
			high-=1
		elif arr[mid]<1:
			print(f'second {arr[mid],arr[low]}')
			arr[mid],arr[low]=arr[low],arr[mid]
			low+=1
			mid+=1
		else:
			mid+=1
		print(arr)

	print(arr)











