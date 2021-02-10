class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        tgt=len(graph)-1
        
        result=[]
        
        def dfs(v,path):
            path+=(v,)
            if v==tgt:
                result.append(list(path))
                return
            for edge in graph[v]:
                dfs(edge,path)
            return
        
        
        dfs(0,tuple())
        
        return result