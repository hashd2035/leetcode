class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        """
        large => len(group) >= 3
        if prev == end, end++
        if not, 
            if length >= 3:
                add prevgroup to ans
            start = end
            
        
        l
        s
         e
        p
        aaa
        abbxxxxzzy
        
        """
        ans = [] # increase order by start index 
        
        start, prev = 0, 0
        for end in range(len(s)):
            if s[prev] != s[end]:
                if end - start >= 3:
                    ans.append([start, prev])
                start = end                
            prev = end
            
        if end - start >= 2:
            ans.append([start, prev])
        return ans
                