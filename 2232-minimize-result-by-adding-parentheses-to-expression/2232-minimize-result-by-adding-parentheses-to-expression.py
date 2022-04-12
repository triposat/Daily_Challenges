class Solution:
    def minimizeResult(self, expression: str) -> str:
        plus = expression.index('+')
        pre = expression[:plus]
        post = expression[plus+1:]
        res = []
        for i in range(len(pre)):
            for j in range(1, len(post)+1):
                res.append(pre[:i]+"*"+"("+pre[i:] +
                           "+"+post[:j]+")"+"*"+post[j:])
        maxi = float('inf')
        ans = ""
        for ele in res:
            ele = ele.strip("*")
            if eval(ele) < maxi:
                ans = ele.replace("*", "")
                maxi = eval(ele)
        return ans