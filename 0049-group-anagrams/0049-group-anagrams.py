class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        '''
        list of strings -> group them together based on anagrams

        Brute Force:
        initialize the result list of lists
        we go through each string in the list add it to the inner list
        and then go  through second loop checking if the outer string anagram is equal to inner string anagram.

        O(n^2)


        instead of doing this construct an anagram mapping which maps word to its anagram
        construct a mapping which maps anagram to index in res array.
        
        '''

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            res[tuple(count)].append(s)

        return list(res.values())

        