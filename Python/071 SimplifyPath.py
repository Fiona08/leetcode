#71 


# Time:  O(n)
# Space: O(n)


# Given an absolute path for a file (Unix-style), simplify it.
#
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"


class stackSol():
    def simplifyPath(self,path):
        split_path=path.split('/')
        simplify_path=[]
        for path_elem in split_path:
            if path_elem=='..' and simplify_path:
                simplify_path.pop()
            elif path_elem!='..' and path_elem!='.' and path_elem:
                simplify_path.append(path_elem)
        return '/'+'/'.join(simplify_path)
