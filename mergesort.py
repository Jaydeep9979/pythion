import math,sys,os,collections,functools,itertools,string
if(os.path.exists('input.txt')):
	sys.stdin=open('input.txt','r')
	sys.stdout=open('output.txt','w')
for testcase in range(int(input())):
	arr=[4,1,5,2,3]
	def merge(left,right):
		print(left,right)
		x=[]
		l=r=0
		while l<len(left) and r<len(right):
			if left[l]>right[r]:
				x.append(right[r])
				r+=1
			else:
				x.append(left[l])
				l+=1
		while l<len(left):
			x.append(left[l])
			l+=1
		while r<len(right):
			x.append(right[r])
			r+=1
		return x


	def mergesort(nums):
		if len(nums)>1:
			mid=len(nums)//2
			left=mergesort(nums[:mid])
			right=mergesort(nums[mid:])
		#	print(nums,left,right)
			nums=merge(left,right)
		#print(nums)
		return nums
	print(mergesort(arr))

			

	
		


	

		

