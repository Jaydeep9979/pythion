class Solution:
    def searchInsert(self, arr: , x: int) -> int:
        first,last=0,len(arr)-1
        ans=len(arr)
        while first<=last:
            mid=(first+last)//2
            if arr[mid]<=x:
                first=mid+1
            else:
                ans=mid
                last=mid-1
        return ans
        