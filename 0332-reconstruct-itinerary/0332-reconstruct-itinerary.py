class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        '''
        bfs queue

        push start node 'JFK'

        for all surrounding nodes, add the node and remove the edge.

        keep adding elements to the visited list 
        '''

        graph = defaultdict(list)

        tickets.sort(reverse = True)
        for  u,v in tickets:
            graph[u].append(v)
        
       
        
        st = ['JFK']

        res = []

        while st:

           u = st[-1]

           if graph[u]:
                st.append(graph[u].pop())
           else:
                res.append(st.pop())
        
        return res[::-1]

        