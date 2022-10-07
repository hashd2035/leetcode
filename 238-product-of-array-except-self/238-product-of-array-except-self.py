class Solution:
    def o_1_space(self, nums):
        p, q = 1, 1
        results = [1] * len(nums)
        
        for i in range(len(nums)):
            results[i] *= p
            results[~i] *= q
            
            p *= nums[i]
            q *= nums[~i]
        
        return results
    
    def accumulate(self, nums):
        lprod = [1] + [*accumulate(nums, operator.mul)]             + [1]
        rprod = [1] + [*accumulate(nums[::-1], operator.mul)][::-1] + [1]
        
        return [lprod[i-1] * rprod[i+1] for i in range(1, len(nums)+1)]
        
    def prefixsum_no_comments(self, nums):
        n = len(nums)
        
        lprod = [nums[0] ]+[1]*(n-1)   
        rprod = [1]*(n-1) + [nums[-1]] 
                
        for i in range(1, n):
            lprod[i] = lprod[i-1] * nums[i]  
            
        for i in reversed(range(n-1)):       
            rprod[i] = rprod[i+1] * nums[i]  
            
        answer = []
        for i in range(n):
            left  = 1 if i == 0     else lprod[i-1]
            right = 1 if i == n-1   else rprod[i+1]
            answer.append(left * right)    
        return answer                

    def prefixsum(self, nums):
        """
        [1][[1]2 3 4 ][1]
        [1][ 1[2]3 4 ][1]
        [1][ 1 2[3]4 ][1]
        [1][ 1 2 3[4]][1]
        """
        n = len(nums)
        
        lprod = [nums[0] ]+[1]*(n-1)   
        rprod = [1]*(n-1) + [nums[-1]] 
        
        print (f'init.lprod={lprod}')   # [1] [1, 1, 1]
        print (f'init.rprod={rprod}')   # [1, 1, 1] [4]
                
        for i in range(1, n):
            lprod[i] = lprod[i-1] * nums[i]  
        print (f'accu.lprod={lprod}')        # [1][2, 6, 24]
            
        for i in reversed(range(n-1)):       #    [2, 1, 0]
            rprod[i] = rprod[i+1] * nums[i]  # [1, 1, 1, 4] 
            """
            i=2, rprod[i+1]=4,  nums[i]=3, so, rprod[2]=12 
            i=1, rprod[  2]=12, nums[i]=2, so, rprod[1]=24
            i=0, rprod[  1]=24, nums[i]=1, so, rprod[0]=24
            """                              
        print (f'accu.rprod={rprod}')        # [24, 24, 12][4]
            
        # answer = [lprod[1]] + [1]*(n-1)      # answer starts from 2nd element as the first is just for calculation
        answer = []
        print(f'init.answer={answer}')       # [2, 1, 1, 1] 
        
        for i in range(n):
            left  = 1 if i == 0     else lprod[i-1]
            right = 1 if i == n-1   else rprod[i+1]
            # answer[i] = left * right
            answer.append(left * right)
        
        print(f'after.answer={answer}')     # [24, 12, 8, 6]  
        
        return answer        
        
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.o_1_space(nums)
