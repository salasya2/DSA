class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visited= {}
        if len(prerequisites) == 0:
            return True
        graph = {i : [] for i in range(numCourses)}
        indegree = [0] * numCourses
        for pre in prerequisites:

            graph[pre[1]].append(pre[0])
            indegree[pre[0]] += 1

        count = 0
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:

            node = queue.popleft()
            count += 1

            for v in graph[node]:

                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        print(count, numCourses)
        return (count == numCourses)

    # O((v+e)) O(v)

# O(n)
        