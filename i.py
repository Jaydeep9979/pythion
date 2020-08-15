class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k>len(arr):
            return max(arr)
        k%=len(arr)
        dic={}
        count1,count2=0,0
        c1,c2=True,True
        while True:
            if arr[0]>arr[1]:
                dic[arr[0]]+=1
                if dic[arr[0]]==k:
                    return arr[0]
                dic[arr[1]]=0
                arr.pop(1)
            else:
                dic[arr[1]]+=1
                if dic[arr[1]]==k:
                    return arr[1]
                dic[arr[0]]=0
                arr.pop(0)
        