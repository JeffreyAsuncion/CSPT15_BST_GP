"""
You are given a binary tree. You need to write a function that can determin if
it is a valid binary search tree.
The rules for a valid binary search tree are:
- The node's left subtree only contains nodes with values less than the node's
value.
- The node's right subtree only contains nodes with values greater than the
node's value.
- Both the left and right subtrees must also be valid binary search trees.
Example 1:
Input:
    5
   / \
  3   7
Output: True

Example 2:
Input:
    10
   / \
  2   8
     / \
    6  12
Output: False
Explanation: The root node's value is 10 but its right child's value is 8.
"""
import math # to get the lower and upper bounds math.inf
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    """iterative solution"""
    def is_valid_BST(self, root):
        # Your code here
        # set up a tuple with a stack and the lowest bounds
        stack, inorder = [], float(-math.inf)

        # while either the stack or the root exists
        while stack or root:
            # while the root exists
            while root:
                # traverse the left of the tree
                # append the root to the stack
                stack.append(root)
                # increment the root to the left
                root = root.left # traversing the left branch like a linked list
            # set the root to what is at the top of the stack
            root = stack.pop()

            # if next element in inorder traversal is smaller that the previous one it is not a BST Binary Search Tree
            if root.value <= inorder:
                # return false
                return False

            # set the in order to the roots value
            inorder = root.value
            # set the root to teh roots right node
            root = root.right # traverse to the right
            # loop will continue down the left leg
        # return true
        return True
    

    """recurvsive solution"""
    def is_valid_BST_recursive(self, root):
            # Your code here
            # default True result as BST
            valid = True
            
            # if left child exists
            if root.left:
                # check that the left child is smaller that the root node
                valid = valid and root.left.value < root.value
                # check not valid
                if not valid:
                    # return not valid
                    return False

                valid = valid and self.is_valid_BST_recursive(root.left)

                # if right child exists
                if root.right:
                    # check that the right child is larger that the root node
                    valid = valid and root.right.value > root.value
                    # check not valid
                    if not valid:
                        # return not valid
                        return False
                    
                    valid = valid and self.is_valid_BST_recursive(root.right)
            
            #return result
            return valid
    

b1 = TreeNode(5)
b1.left = TreeNode(3)
b1.right = TreeNode(7)

b2 = TreeNode(10)
b2.left = TreeNode(2)
b2.right = TreeNode(8)
b2.right.left = TreeNode(6)
b2.right.right = TreeNode(12)

print(b1.is_valid_BST(b1)) # True
print(b2.is_valid_BST(b2)) # False

print(b1.is_valid_BST_recursive(b1)) # True
print(b2.is_valid_BST_recursive(b2)) # False