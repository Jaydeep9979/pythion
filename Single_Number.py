import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

import math
for testcase in range(int(input())):
    arr=list(map(int,input().split()))
    x=0
    for i in arr:
        x^=i
    print(x)
