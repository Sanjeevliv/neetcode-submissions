class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        groups=[]
        partial_group=[]
        used=[]
        
        for i in range(n):
            if strs[i] not in used:
                if len(strs)==1:
                    return [[strs[i]]]

                partial_group.append(strs[i])
                used.append(strs[i])
                
                for j in (x for x in range(i+1,n) if x not in used):
                    if sorted(strs[i])==sorted(strs[j]):
                        partial_group.append(strs[j])
                        used.append(strs[j])
                groups.append(partial_group)
                partial_group=[]
        return groups