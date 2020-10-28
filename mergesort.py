import math,sys,os,collections,functools,itertools,string
if(os.path.exists('input.txt')):
	sys.stdin=open('input.txt','r')
	sys.stdout=open('output.txt','w')
for testcase in range(int(input())):
	arr=[2,4,3,5,1]
	count=0
	def merge(left,right):
		print(left,right)
		global count
		x=[]
		l=r=0
		while l<len(left) and r<len(right):
			if left[l]>right[r]:
				x.append(right[r])
				if left[l]>2*right[r]:
					count+=len(left)-l
				r+=1
			else:
				x.append(left[l])
				l+=1
		while l<len(left):
			if left[l]>2*right[r-1]:
					count+=len(left)-l
			x.append(left[l])
			l+=1
		while r<len(right):
			if left[l]>2*right[r-1]:
					count+=len(left)-l
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
	print(count)

		

	
		


	

		

