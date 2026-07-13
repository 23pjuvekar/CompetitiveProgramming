class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        se = set()
        folder.sort(key=len)
        for f in folder:
            c = f.split("/")
            curr = "/"
            add = True
            for s in c:
                if s == "":
                    continue
                curr += s
                if curr in se:
                    add = False
                    break
                curr += "/"
            if add:
                se.add(f)
        return list(se)
