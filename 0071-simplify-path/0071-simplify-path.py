class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Rules 
            /   - starts    - meaning we can split tokens by /
            //  - single /  - will throw away except one /
            .   - current   - will throw away
            ..  - above     - pop the previous and throw away
            ... - file/dir  - will be appended
            else- file/dir  - will be appended
            path don't end with /
            
            e.g. 
            /home/      => /home
            /../        => /
            /home//foo/ =>/home/foo
        
        clarification 
            /..home => ..home is file/dir
            /.home  => .home is file/dir
            /hom.me => hom.me is file/dir
            /home./ => home. is file/dir

        The answer: The question said "any other format of periods" is the file/dir
        """
        
        stack = []
    
        for token in path.split('/'):
            if token == '..':
                if stack: stack.pop()
            elif token == '.' or not token:
                continue
            else:
                stack.append(token)
            
        return "/" + "/".join(stack)