class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        maps=collections.defaultdict(list)
        for i in arr:
            maps[i%k].append(i)
        if 0 in maps:
            if len(maps[0])%2!=0:
                return False
        if k%2==0:
            if k//2 in maps:
                if len(maps[k//2])!=0:
                    return False
        for key in maps.keys():
            if key!=0 and key!=k//2:
                x=maps.get(key,[])
                y=maps.get(k-key,[])
                if len(x)!=len(y):
                    return False
        return True
            