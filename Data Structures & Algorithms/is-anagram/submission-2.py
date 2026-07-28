class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        sht = {}
        tht = {}

        for i in range(len(s)):
            if(s[i] in sht.keys()):
                sht[s[i]] += 1
            else:
                sht[s[i]] = 1

            if(t[i] in tht.keys()):
                tht[t[i]] += 1
            else:
                tht[t[i]] = 1

        return sht == tht