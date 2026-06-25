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

        word2ana = defaultdict(str)
        anag2idx = {}

        res = []

        for word in strs:

            word2ana[word] = "".join(sorted(word))
        
        for word in strs:

            if word2ana[word] not in anag2idx:
                res.append([word])
                anag2idx[word2ana[word]] = len(res) - 1
            
            else:
                res[anag2idx[word2ana[word]]].append(word)

        return res

        