class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        res = []
        n = len(heights)
        m = len(heights[0])

        queue = deque([])
        visited = defaultdict(int)
        for i in range(n):
            visited[(i, 0)] = -1
            queue.append([i, 0])

        for j in range(1, m):
            visited[(0, j)] = -1
            queue.append([0, j])

        DIR = [[-1, 0], [1, 0], [0, 1], [0, -1]]
       
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in DIR:
                    nr = dr + r
                    nc = dc + c

                    if (
                        nr < 0
                        or nc < 0
                        or nr >= n
                        or nc >= m
                        or heights[r][c] > heights[nr][nc]
                        or visited[(nr, nc)] == -1
                    ):
                        continue

                    queue.append([nr, nc])
                    visited[(nr, nc)] = -1

        for i in range(n):
            if visited[(i, m - 1)] == -1:
                visited[(i, m - 1)] = -3
                res.append([i, m - 1])
            else:
                visited[(i, m - 1)] = -2
            queue.append([i, m - 1])

        for j in range(m - 1):
            if visited[(n - 1, j)] == -1:
                visited[(n - 1, j)] = -3
                res.append([n - 1, j])
            else:
                visited[(n - 1, j)] = -2
            queue.append([n - 1, j])

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in DIR:
                    nr = dr + r
                    nc = dc + c

                    if (
                        nr < 0
                        or nc < 0
                        or nr >= n
                        or nc >= m
                        or heights[r][c] > heights[nr][nc]
                        or visited[(nr, nc)] == -2
                        or visited[(nr, nc)] == -3
                    ):
                        continue

                    queue.append([nr, nc])
                    if visited[(nr, nc)] == -1:
                        visited[(nr, nc)] = -3
                        res.append([nr, nc])
                    else:
                        visited[(nr, nc)] = -2

        return res
