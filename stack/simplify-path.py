class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = []
        old = path.split('/')
        for d in old:
            if not d or d == '.':
                continue
            if d == '..':
                if dirs:
                    dirs.pop()
            else:
                dirs.append(d)

        return '/' + '/'.join(dirs)

