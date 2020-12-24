class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        
        t1= int(abs(C-A)*abs(D-B))
        t2= int(abs(G-E)*abs(H-F))
        i= int(max(min(C,G)-max(A,E),0)*max(min(D,H)-max(B,F),0))
        
        return t1+t2-i