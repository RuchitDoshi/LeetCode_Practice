class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph={i:[] for i in range(numCourses)}
        
        for a,b in prerequisites:
            graph[a].append(b)
            
        visited=[0]*numCourses
        
        def dfs(v):
            
            if visited[v]==-1:
                return False
            if visited[v]==1:
                return True
            
            visited[v]=-1
            for a in graph[v]:
                if not dfs(a):
                    return False
            
            visited[v]=1
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True