class Solution:
    """
    count = 11
                        
    internationalization, i12iz4n
    
                       _
    internationalization
          _
    i5a11o1
    
    [edge cases]
    multiple digits
    digit in the beginning
    digit in the middle
    digit in the end !!!!! - I made an assumption that this case won't occur. which is wrong
    
    """
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w, a = 0, 0
        count = ""
        while a < len(abbr):
            if abbr[a].isalpha():
                # if prefix is number
                if len(count) > 0:
                    w += int(count)
                    count = ""
                  
                if w >= len(word) or abbr[a] != word[w]:
                    return False
                
                a += 1
                w += 1

            elif abbr[a].isdigit():
                if abbr[a] == '0' and len(count) == 0:
                    return False
                count += abbr[a]  
                a += 1
                
        if len(count) > 0:
            w += int(count)
        
        return w == len(word) and a == len(abbr)