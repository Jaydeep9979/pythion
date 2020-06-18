import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

import math
for testcase in range(int(input())):
    arr=list(map(int,input().split()))
    xor=0
    for i in arr:
        xor^=i
    print(xor)
