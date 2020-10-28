import math,sys,os,collections
if(os.path.exists('input.txt')):
	sys.stdin=open('input.txt','r')
	sys.stdout=open('output.txt','w')
for testcase in range(int(input())):
	arr=[5,2,6,1]
	count=0
	def merge(ans,left,right):
		global count
		temp=[]
		i=0
		j=0
		while i<len(left) and j<len(right):
			if left[i][1]>right[j][1]:
				temp.append(left[i])
				ans[left[i][0]]+=len(right)-j
				i+=1
			else:
				temp.append(right[j])
				#ans[right[j][0]]+=len(left)-i
				j+=1
		while i<len(left): 
			temp.append(left[i])
			i+=1
		while j<len(right):
			temp.append(right[j])
			j+=1
		return temp
	def merge_sort(arr):
		if len(arr)>1:
			mid=len(arr)//2
			left=merge_sort(arr[:mid])
			right=merge_sort(arr[mid:])
			return merge(ans,left,right)
		return arr
	arr=merge_sort(arr)
	count=[]
	print(count)









