import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')


for testcase in range(int(input())):
    arr = list(map(int, input().split()))
    arr.sort()
    dp = [1 for i in range(len(arr))]
    ans = [-1 for i in range(len(n))]
    for i in range(1, len(arr)):
        for j in range(i):
            if n[i] == 1 or (arr[i] % arr[j] == 0 and dp[i] < dp[j]+1):
                dp[i] = dp[j]+1
                ans[i] = j
    
    x = []
    n = max(dp)
    i = dp.index(n)
    while i != -1:
        x.append(arr[i])
        i = ans[i]
    x.reverse()
    print(x)
