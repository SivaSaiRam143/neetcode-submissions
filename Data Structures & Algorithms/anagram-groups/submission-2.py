class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # The catch here is, we need to do the hash map grouping. i.e, we need group the hashes by key as hash tuple and value as its words
        # list is mutable, so can't be used as hash key
        # so we convert that to tuple, which is immutable to use as hash key

        ans_dict = {}
        c_hashes = [[0]*26 for x in strs]
        for i,st in enumerate(strs):
            for x in st:
                c_hashes[i][ord(x)-ord('a')] += 1
            hash_tuple = tuple(c_hashes[i])
            if hash_tuple in ans_dict:
                ans_dict[hash_tuple].append(st)
            else:
                ans_dict[hash_tuple] = [st]
        return list(ans_dict.values())
