#TWO SUM
nums=list(map(int,input().split())) 
target=int(input())
n=len(nums)
for i in range(0,n): #T.C:-O(N)
    for j in range(i+1,n): #T.C:-O(N)
        if(nums[i]+nums[j]==target):
            print(i,j)  #total T.C:-O(N*N)=O(N*2)
