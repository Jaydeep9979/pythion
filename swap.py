import math,sys,os,collections
if(os.path.exists('input.txt')):
	sys.stdin=open('input.txt','r')
	sys.stdout=open('output.txt','w')
for testcase in range(int(input())):
    s=[1, 3, 0, 5, 8, 5]
    f=[2, 4, 6, 7, 9, 9]
    # s=[75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
    # f=[112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]
    time=[]
    for i in range(len(s)):
        start=s[i]
        finish=f[i]
        time.append((start,finish,i+1))
    time.sort(key=lambda x :x[1])
    mn,mx=time[0][0],time[0][1]
    ans=[time[0][2]]
    for start,finish,meet_no in time[1:]:
        if start>mx:
            ans.append(meet_no)
            mx=finish
    for i in time:
        print(i)
    print(ans)  