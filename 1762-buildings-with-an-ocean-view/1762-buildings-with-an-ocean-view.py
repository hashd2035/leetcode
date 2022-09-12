class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        st = deque()
        
        """
             _
          i= 0,1,2,3             
          h= 1,3,2,4         

          s= 
     pre_h = 
        ans= 
        """
        for i, cur in enumerate(heights): # 1, 3, 2, 4
            while st and heights[st[-1]] <= cur: # heights[1]==3 < 3  
                pre = st.pop()                
            st.append(i) # 1
        return st
