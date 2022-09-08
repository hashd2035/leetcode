class FileSystem:

    def __init__(self):
        self.internal = {}
        

    def createPath(self, path: str, value: int) -> bool:
        if path in ["", "/"]:
            return False
        if path in self.internal:
            return False
        parent = path[:path.rfind("/")] 
        
        if len(parent) > 0 and parent not in self.internal:
            return False
        
        self.internal[path] = value
        return True

    def get(self, path: str) -> int:
        if path not in self.internal:
            return -1
        return self.internal[path]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)