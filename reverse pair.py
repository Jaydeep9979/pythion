class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count=0
        def merge_sort(arr):
            mid=len(arr)//2
            if not mid:
                return arr
            left=merge_sort(arr[:mid])
            right=merge_sort(arr[mid:])
            l=r=lc=0
            for i in range(len(arr)):
                if r==len(right) or (l<len(left)  and left[l]<=right[r]):
                    nums[i]=left[l]
                    l+=1
                else:
                    nums[i]=right[r]
                    while lc<len(left) and left[lc]<=2*right[r]:
                        lc+=1
                    self.count+=len(left)-lc
                    r+=1
            return nums
        merge_sort(nums)
        return self.count
    