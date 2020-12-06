"""
You are given a binary tree.
Write a function that can find the **maximum depth** of the binary tree. The
maximum depth can be defined as the number of nodes found along the longest
path from the root down to the furthest leaf node. Remember, a leaf node is a
node that has no children.
Example:
Given the following binary tree
    5
   / \
  12  32
     /  \
    8    4
your function should return the depth = 3.
"""
class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    """ #1"""
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinaryTreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinaryTreeNode(value)
            else:
                self.right.insert(value)


    def maxDepth(self, root):
        """ #1"""
        # Your code here -      O(n)
        # base case of empty tree?
        if root is None:
            return 0        
        # get left height
        left_height = self.maxDepth(root.left)

        # get right height
        right_height = self.maxDepth(root.right)

        # return the max of left height and right height + 1
        return max(left_height,right_height) + 1 # this is the increment or counter
        #######################################################
        # # use a stack for storage -          O(n)
        # stack = []

        # # base case
        # if root is not None:
        #     stack.append((1, root))


        # # set a depth counter?
        # depth = 0
        
        # # while our stack is not empty?
        # while stack != []:
        #     # pop the stack to the current depth and the current root node
        #     current_depth, root = stack.pop()
            
        #     # if our root node is not none
        #     if root is not None:
        #         # set the depth to the max of depth and current depth
        #         depth = max(depth, current_depth)
        #         # append the current depth + 1 and the root left to the stack 
        #         stack.append((current_depth + 1, root.left))
        #         # append the current depth + 1 and the root right to the stack 
        #         stack.append((current_depth + 1, root.right))
        # # return the depth
        # return depth


"""This is how to do it without the insert Method"""
b1 = BinaryTreeNode(5)
b1.left= BinaryTreeNode(12)
b1.right= BinaryTreeNode(32)
b1.right.left = BinaryTreeNode(8)
b1.right.right = BinaryTreeNode(3)
# b1.right.right.right = BinaryTreeNode(1)

print(b1.maxDepth(b1))





