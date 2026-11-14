class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        open_ls = ['(', '{', '[']
        close_ls = {')': '(', '}': '{', ']': '['}
        if s[0] in close_ls:
            return False
        
        st.append(s[0])
        for i in range(1, len(s)):
            if s[i] in open_ls:
                st.append(s[i])
            elif s[i] in close_ls.keys() and st and st[-1] == close_ls[s[i]]:
                st.pop()
            else:
                return False

        if len(st) > 0 :
            return False

        return True