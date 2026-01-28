class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        count1 = defaultdict(int)
        count2 = defaultdict(int)


        for c in t:

            count1[c] += 1

        need = len(count1)

        res = ""
        resLen = float("inf")

        have = 0
        i = 0
        for j in range(len(s)):

            count2[s[j]] += 1

            # print(count2, count1)

            if s[j] in count1 and count1[s[j]] == count2[s[j]]:
                have += 1

            while have == need:
                # print(s[i],s[j])

                if resLen > j - i + 1:
                    
                    resLen = j - i + 1
                    res = s[i:j+1]
                
                count2[s[i]] -= 1

                if s[i] in count1 and count1[s[i]] > count2[s[i]]:
                    have -= 1
                i+=1

        return res
        