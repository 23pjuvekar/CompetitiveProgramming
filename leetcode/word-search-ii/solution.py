class TreeNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TreeNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Fill up Trie Struct with words
        root = TreeNode()
        for word in words:
            root.addWord(word)

        # Run DFS adding word it it matches
        ROWS = len(board)
        COLS = len(board[0])
        visted = set()
        res = set()

        def dfs(r, c, node, word):
            # Base Case
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visted or board[r][c] not in node.children:
                return

            # Add stuff
            visted.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            # RUN DFS in 4 directions
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            # Backtrack
            visted.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)
