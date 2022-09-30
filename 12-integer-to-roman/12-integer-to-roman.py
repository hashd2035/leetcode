class Solution:
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
        while num > 0:
            for roman, digit in Romans:
                d, m = divmod(num, digit)
                if d >= 1:
                    num = num - digit
                    ans.append(roman)
                    break
        return ''.join(ans)