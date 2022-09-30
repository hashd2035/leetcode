class Solution:
    
    """
    1. if we can find the value that is largest, but, smaller, then pick this.
        * How do we know the value is smaller? 
            - if `140 / Roman == 1`, then, Roman is smaller than number.
        * How do we know the largest?
            * if we can go through Romans from largest to smaller and the first smaller is largest smaller
    2. Once, we find the largest smaller, we can subtract `largest, smaller` from num, then, repeat
    """    
    def intToRoman(self, num: int) -> str:
        """
        num needs to be divisible by the largest available
        """
        Romans = [("M", 1000), ("CM", 900), 
                 ("D", 500), ("CD", 400), 
                 ("C", 100), ("XC", 90), 
                 ("L", 50), ("XL", 40), 
                 ("X", 10), ("IX", 9), 
                 ("V", 5), ("IV", 4), 
                 ("I", 1)] 
        
        ans = []
        for roman, digit in Romans:
            # We don't want to continue looping if we're done.
            if num == 0: 
                break
            count, num = divmod(num, digit)

            # Append "count" copies of "symbol" to roman_digits.
            ans.append(roman * count)
        return "".join(ans)
