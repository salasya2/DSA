class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = [[] for i in range(numCourses)]
        indegree = [0]*numCourses


        for u,v in prerequisites:
            graph[u].append(v)
            indegree[v]+=1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        res = []
        finish = 0
        while q:

            u = q.popleft()
            finish += 1
            res.append(u)

            for v in graph[u]:

                indegree[v] -=1
                if indegree[v] == 0:
                    q.append(v)
        
        return res[::-1] if finish == numCourses else []
