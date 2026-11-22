class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        def helper(ind,ope,clos,curr):
            if clos==ind:
                ans.append(curr)
                return
            if ope<n:
                helper(ind,ope+1,clos,curr+'(')
            if ope>clos:
                helper(ind,ope,clos+1,curr+')')
        helper(n,0,0,"")
        return ans