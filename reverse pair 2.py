import math,sys,os,collections
if(os.path.exists('input.txt')):
	sys.stdin=open('input.txt','r')
	sys.stdout=open('output.txt','w')
for testcase in range(int(input())):
    count=0
    nums=[4,3,2]
    def mergeSort(nums):
        global count
        m=len(nums)//2
        if not m: return nums
        left=mergeSort(nums[:m])
        right=mergeSort(nums[m:])
        l=r=lc=0
        for i in range(len(nums)):
            if r==len(right) or (l<len(left) and left[l]<=right[r]):
                nums[i]=left[l]
                l+=1
            else:
                nums[i]=right[r]
                while lc<len(left) and left[lc]<=right[r]: lc+=1
                count+=len(left)-lc
                r+=1
        return nums
    mergeSort(nums)
    print(count)