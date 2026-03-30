# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root==None):
            return []
        queue=[root]
        ans=[]
        while(len(queue)>0):
            level=[]
            for i in range(len(queue)):
                popnode=queue.pop(0)
                if(popnode.left!=None):
                    queue.append(popnode.left)
                if(popnode.right!=None):
                    queue.append(popnode.right)
                level.append(popnode.val)
            ans.append(level)
        return ans
