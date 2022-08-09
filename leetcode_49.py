class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mymap = dict()
        
        for s in strs:
            var = ''.join(sorted(s))
            if var not in mymap:
                mymap[var] = [s]
            else:
                mymap[var].append(s)
                
        return mymap.values()