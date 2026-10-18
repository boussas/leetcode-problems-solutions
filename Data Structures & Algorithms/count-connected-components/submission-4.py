class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def explore(graph,node,visited):
            if node in visited:
                return False
            visited.add(node)
            for nei in graph[node]:
                explore(graph,nei,visited)
            return True
        
        graph=defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        print(graph)
        res=0
        visited=set()
        for node in range(n):
            if node not in visited:
                explore(graph,node,visited)
                res+=1
        return res
