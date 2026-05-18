class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""
class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = word
        

    def search(self, word):

        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return (len(curr.word) > 0)
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        for word in words:
            self.insert(word)
        
        res = set()
        temp = ""
        curr = self.root
        
        def helper(curr, board, i, j,words):

            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0 : 
                return
            if board[i][j] not in curr.children:
                return
            
            curr = curr.children[board[i][j]]
            if len(curr.word) > 0:
                res.add(curr.word)
            old_char = board[i][j]
            board[i][j] = '#'
            helper(curr,board,i+1,j,words)
            helper(curr,board,i-1,j,words)
            helper(curr,board,i,j+1,words)
            helper(curr,board,i,j-1,words)
            board[i][j] = old_char
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in curr.children:
                    # print("going in")
                    helper(curr, board, i, j, words)

        return list(res)
            

        


        