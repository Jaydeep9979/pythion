def getMaxArea(w, h, boundaryType, boundaryDist):
        ans=[]
        a1,a2=[],[]
        for t,dist in zip(boundaryType,boundaryDist):
            if t==0:
                a1.append(dist)
                max1=a1[0]
                for i in range(1,len(a1)):
                    max1=max(max1,a1[i]-a1[i-1])
                besth=max1
            else:
                a2.append(dist)
                max1=a2[0]
                for i in range(1,len(a2)):
                    max2=max(max2,a2[i]-a2[i-1])
                bestw=max2
        
            ans.append(besth*bestw)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    w = int(input().strip())

    h = int(input().strip())

    boundaryType_count = int(input().strip())

    boundaryType = []

    for _ in range(boundaryType_count):
        boundaryType_item = int(input().strip()) != 0
        boundaryType.append(boundaryType_item)

    boundaryDist_count = int(input().strip())

    boundaryDist = []

    for _ in range(boundaryDist_count):
        boundaryDist_item = int(input().strip())
        boundaryDist.append(boundaryDist_item)

    result = getMaxArea(w, h, boundaryType, boundaryDist)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
    