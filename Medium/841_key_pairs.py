class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        num=len(rooms)
        visited=[0]*num
        
        def dfs(v):
            if visited[v]==1:
                return

            visited[v]=1
            for a in rooms[v]:
                dfs(a)
            
            return 
                
        
        
        dfs(0)
        
        if sum(visited)==num:
            return True
        
        return False
        