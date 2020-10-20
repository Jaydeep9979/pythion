import math,sys,os,collections
if(os.path.exists('input.txt')):
	sys.stdin=open('input.txt','r')
	sys.stdout=open('output.txt','w')
for testcase in range(int(input())):
    scores = [1,3,5,10,15]
    ages = [1,2,3,4,5]
    age_score=sorted(zip(ages,scores))
    print(age_score)
    dp=[x[1] for x in age_score]
    print(dp)
    for i in range(len(scores)):
        #dp[i]=age_score[i][1]
        for j in range(i):
            if age_score[i][1]>=age_score[j][1] and  dp[i]<dp[j]+age_score[i][1]:
                dp[i]=dp[j]+age_score[i][1]
    print(dp)
    print(max(dp))