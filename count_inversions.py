import math,sys,os,collections
if(os.path.exists('input.txt')):
	sys.stdin=open('input.txt','r')
	sys.stdout=open('output.txt','w')
for testcase in range(int(input())):
	arr=list(map(int,input().split()))
	def merge(arr,temp,left,mid,right):
		i,j,k=left,mid,left
		inv=0
		while (i <=mid-1) and (j<=right):
			if arr[i]<=arr[j]:
				temp[k]=arr[i]
				i+=1
			else:
				temp[k]=arr[j]
				j+=1
				inv+=(mid-i)
			k+=1
		while i<=mid-1:
			temp[k]=arr[i]
			k+=1
			i+=1
		while j<=right:
			temp[k]=arr[j]
			k+=1
			j+=1
		for  i in range(left,right+1):
			arr[i]=temp[i]
		return inv

	def merge_sort(arr,temp,left,right):
		inv=0
		if right>left:
			mid=(right+left)//2
			inv+=merge_sort(arr,temp,left,mid)
			inv+=merge_sort(arr,temp,mid+1,right)
			inv+=merge(arr,temp,left,mid+1,right)	
		return inv

	temp=[None]*(len(arr))
	print(merge_sort(arr,temp,0,len(arr)-1))


