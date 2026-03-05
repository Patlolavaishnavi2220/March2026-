def combinationsum(candidates,target):
    def generate(ind,curr_subset,ans,candidates,target):
        if(target==0):
            ans.append(curr_subset.copy())
            return
        if(target<0):
            return
        if(ind==len(candidates)):
            return
        curr_subset.append(candidates[ind])
        generate(ind,curr_subset,ans,candidates,target-candidates[ind])
        curr_subset.pop()
        generate(ind+1,curr_subset,ans,candidates,target)
    ind=0
    ans=[]
    curr_subset=[]
    generate(ind,curr_subset,ans,candidates,target)
    return ans
candidates=list(map(int,input().split()))
target=int(input())
print(combinationsum(candidates,target))
