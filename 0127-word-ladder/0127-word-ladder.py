class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        
        
        n = len(wordList)
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        graph = defaultdict(list)
        for word in wordList:

            for i in range(len(word)):

                pattern = word[:i] + '*' + word[i+1:]

                graph[pattern].append(word)
        
        res = 0
        queue = deque([beginWord])
        visited = set()
        visited.add(beginWord)

        while queue:
            res +=1
            for i in range(len(queue)):
                
                word = queue.popleft()

                if word == endWord:
                    return res
                
            
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    if pattern in visited:
                        continue
                    visited.add(pattern)
                    for nei_word in graph[pattern]:
                        if nei_word not in visited:
                            queue.append(nei_word)   
                            visited.add(nei_word)    
        return 0
    
    #O(n*m + m)    #O(n*m + m) 

        