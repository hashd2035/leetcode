class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        valid
        
        _
        ((le)etco)de
    st    
   ans     
        ()leetcode
        
        invalid
        - if s doesn't have any character apart from '(' or ')'
        - cannot start with ')'
        - cannot end with '('
        - # of open and close bracket has to be same
        """
        
        st = deque()
        remove = set()
        
        for i, c in enumerate(s):
            if not st:
                if c == ')':
                    remove.add(i)
                elif c == '(':
                    st.append(i)
            else:
                if c == ')':
                    st.pop()
                elif c == '(':
                    st.append(i)
                    
        while st:
            remove.add(st.pop())
        
        ans = []
        for i, c in enumerate(s):
            if i not in remove:
                ans.append(c)
        
        return ''.join(ans)
        
            