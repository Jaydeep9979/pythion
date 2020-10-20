import math,sys,os,collections
if(os.path.exists('input.txt')):
	sys.stdin=open('input.txt','r')
	sys.stdout=open('output.txt','w')
for testcase in range(int(input())):
    arr=list(map(int,input().split()))
    arr=[2,4,3,5,1]
    count=0
    def merge(left,right):
        global count
        ans=[]
        i=0 
        j=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                ans.append(left[i]) 
                i+=1
            else:
                ans.append(right[j])
                if left[i]>(2*right[j]):
                    count+=len(left)-i
                j+=1
        while i<len(left):
            ans.append(left[i])
            i+=1
        while j<len(right):
            ans.append(right[j])
            j+=1
        return ans
    def merge_sort(arr):
        if len(arr)>1:
            mid=len(arr)//2
            left=merge_sort(arr[:mid])
            right=merge_sort(arr[mid:])
            return merge(left,right)
        return arr
    merge_sort(arr)
    print(count)

