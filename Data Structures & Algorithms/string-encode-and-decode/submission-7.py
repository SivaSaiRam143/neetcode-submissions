class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        key = 4
        ans = []
        ans_lens = []
        for st in strs:
            c_st = ""
            for x in st:
                c_st += str(chr((ord(x)+key)%256))
            ans.append(c_st)
            ans_lens.append(str(len(c_st)))
        res = [str(ans_lens[i])+"@"+ans[i] for i in range(len(ans))]
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        if s == "": return []
        key=4
        ans = []
        s_len = ""
        i = 0
        print(s)
        while i<len(s):
            if s[i] == "@":
                print(s[i+1:i+1+int(s_len)])
                cur_s = s[i+1:i+1+int(s_len)]
                decoded_str = ""
                for x in cur_s:
                    decoded_str += str(chr((ord(x)-key)%256))
                print(decoded_str)
                ans.append(decoded_str)
                i=i+1+int(s_len)
                s_len = ""
            else:
                s_len += s[i]
                i+=1
        return ans


