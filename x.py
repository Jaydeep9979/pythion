n=int(input())
arr=list(map(int,input().split()))
target=max(arr)
count=0
while arr:
	ind=arr.index(target)
	if len(arr)==1:
			count+=arr
			arr.pop()
			break
	else:
			if ind==0:
					count+=(target*arr[1])
					arr.pop(1)
			elif ind==len(arr)-1:
					count+=(target*arr[-2])
			else:
					count+=target*max(arr[ind-1],arr[ind+1])+min(arr[ind-1],arr[ind+1])
					if arr.index(max(arr[ind-1],arr[ind+1]))==ind-1:
							arr.pop(ind-1)
					else:
							arr.pop(ind+1)
print(count,end="")  