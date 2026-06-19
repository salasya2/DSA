class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for src, dest in prerequisites:

            adj[src].append(dest)
            indegree[dest] += 1
        
        finish = 0
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        while q:
            node = q.popleft()
            finish += 1

            for neigh in adj[node]:
                indegree[neigh] -= 1

                if indegree[neigh] == 0:
                    q.append(neigh)

        return finish == numCourses 
            