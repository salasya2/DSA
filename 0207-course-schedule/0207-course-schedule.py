class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        
        n = len(prerequisites)
        if n == 0:
            return True
        graph = defaultdict(list)

        for i in prerequisites:

            c1 = i[0]
            c2 = i[1]
            graph[c1].append(c2)
            
        
        visited = defaultdict(bool)

        def dfs(u):
            
            if visited[u] == True:
                return False
            
            if len(graph[u]) == 0:
                return True

            visited[u] = True
            for v in graph[u]:
                if not dfs(v):
                    return False
            visited[u] = False
            graph[u] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True




        