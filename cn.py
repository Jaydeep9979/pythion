import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

import math,bisect
from sortedcontainers import SortedList
for testcase in range(int(input())):
    rains=list(map(int,input().split()))
    s=SortedList()
    checkrain={}
    ans=[1 for i in range(len(rains))]
    for day,lake in enumerate(rains):
        if lake==0:
            s.add(day)
        else:
            if checkrain.get(lake,-1)==(-1):
                ans[day]=-1
                checkrain[lake]=day
            else:
                x=bisect.bisect_right(s,checkrain[lake])
                if x==len(s):
                    print([])
                else:
                    ans[s[x]]=lake
                    ans[day]=-1
                    s.discard(s[x])
                # if s and checkrain[lake]<s[0]<day:
                #     ans[s[0]]=lake
                #     ans[day]=-1
                #     s.discard(s[0])
                # else:
                #     print([])
                #     break

        
    print(ans)












        