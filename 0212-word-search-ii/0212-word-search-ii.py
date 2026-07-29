class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.isEnd += 1
    
    def search(self, word):

        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.isEnd


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie  = Trie()

        for word in words:
            trie.insert(word)
        res = []
        def backtrack(r,c,curr):
            nonlocal n,m
            val = board[r][c]
            board[r][c] = "#"
            
            if curr.isEnd:
                curr.isEnd -= 1
                res.append("".join(word))

            for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:

                nr, nc = dr + r, dc + c

                if nr < 0 or nc < 0 or nr >= n or nc >=m or board[nr][nc] not in curr.children or board[nr][nc] == "#":
                    continue
                word.append(board[nr][nc])
            
                backtrack(nr,nc,curr.children[board[nr][nc]])
                word.pop()
            board[r][c] = val


        root = trie.root
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                curr = root
                
                if board[i][j] in curr.children:
                    word = [board[i][j]]
                    backtrack(i,j,curr.children[board[i][j]])
        return res
                       