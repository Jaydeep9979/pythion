for testcase in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    odd=0
    even=0
    for i,val in enumerate(arr):
        if i%2==0:
            if val%2!=0:
                even+=1
        else:
            if val%2==0:
                odd+=1
    if odd==even:
        print(odd)
    else:
        print(-1)
