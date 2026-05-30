class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c_hashes = [{} for x in strs]
        for i,st in enumerate(strs):
            for x in st:
                c_hashes[i][x] = c_hashes[i].get(x,0)+1
        ans = []
        for i in range(len(c_hashes)):
            if c_hashes[i] != -1:
                cur_ans = [strs[i]]
                for j in range(i+1, len(c_hashes)):
                    if c_hashes[i] == c_hashes[j]:
                        cur_ans.append(strs[j])
                        c_hashes[j] = -1
                ans.append(cur_ans)
        return ans