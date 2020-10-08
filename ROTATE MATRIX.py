import sys,os
if(os.path.exists('input.txt')):
    sys.stdin=open('input.txt','r')
    sys.stdout=open('output.txt','w')
for testcase in range(int(input())):
    arr=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    n=len(arr)
    #123  741
    #456  852
    #789  963
    for layer in range(n//2  +1):
        for j in range(layer,((n)-(layer))-1):
           #print(arr[layer][j],arr[n-j-1][layer],arr[n-layer-1][n-j-1],arr[j][n-1-layer])
            temp=arr[layer][j]#(0,0)(0,1)
            arr[layer][j]=arr[n-j-1][layer]#(3,0)(2,0)
            arr[n-j-1][layer]=arr[n-layer-1][n-j-1]#(3,3)(3,2)
            arr[n-layer-1][n-j-1]=arr[j][n-1-layer]#(0,3)(1,3)
            arr[j][n-1-layer]=temp
    for i in arr:
        print(i)
         
        




