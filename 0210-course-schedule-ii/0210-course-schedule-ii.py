class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        graph = {i : [] for i in range(numCourses)}

        res = []

        indegree = [0] * numCourses
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            indegree[pre[0]] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:

            curr = queue.popleft()
            res.append(curr)

            for v in graph[curr]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        if len(res)!= numCourses:
            return []
        return res