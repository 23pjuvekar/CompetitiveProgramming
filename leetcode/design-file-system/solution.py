class FileSystem:

    def __init__(self):
        self.paths = {}

    def createPath(self, path: str, value: int) -> bool:
        if path in self.paths:
            return False
        files = path.split("/")
        curr = ""
        for f in files[:len(files) - 1]:
            if f == "":
                continue
            curr += "/" + f
            if curr not in self.paths:
                return False
        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        if path in self.paths:
            return self.paths[path]
        return -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
