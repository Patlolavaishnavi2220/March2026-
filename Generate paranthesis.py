def generateparanthesis(n):
    def generate(curr_str,ans,open,close,n):
        if(open+close==2*n and open==close):
            ans.append(curr_str)
            return
        if(open>n):
            return
        if(close>open):
            return
        generate(curr_str+"(",ans,open+1,close,n)
        generate(curr_str+")",ans,open,close+1,n)
    ans=[]
    curr_str=""
    open=0
    close=0
    generate(curr_str,ans,open,close,n)
    return ans
n=int(input())
print(generateparanthesis(n))
