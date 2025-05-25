# Last updated: 5/25/2025, 1:08:21 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive Solution (Depth-first traversal)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # # Base case: root is null
        # if root == None:
        #     return None
        # left = self.invertTree(root.left)
        # right = self.invertTree(root.right)
        # root.left = right
        # root.right = left

        # Iterative Solution (Breadth-first traversal)
        # Use a queue to store references to nodes
        # 1. Root node into queue,
        if not root:
            return None 
        queue = collections.deque([root])
        # 2. ask queue for a node,
        while queue:
            current = queue.popleft()
            # 3. swap its children and 
            current.left, current.right = current.right, current.left 
            # 4. place them in the queue
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        # 5. repeat until queue is empty
        return root


        return root



        
