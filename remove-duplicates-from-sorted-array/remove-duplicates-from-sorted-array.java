class Solution {
    public int removeDuplicates(int[] nums) {
        int w = 0;
        
        /**
        12345
          r
          w
        
        11122
            r
         w
        12
        */
        
        for (int r = 0; r < nums.length; r++) {
            // if (nums[r] == nums[w]) {
            //     continue();    
            // } else {
            //     w += 1;
            // }
            if (nums[r] != nums[w]) w += 1;
            nums[w] = nums[r];
        }
        return w+1;
            
    }
}