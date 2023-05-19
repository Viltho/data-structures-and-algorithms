class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value
        
class TreeNode:
    def __init__(self):
        self.root = None
            
    # def preorder(self, root):
    #     if root is not None:
    #         print(root.value), self.preorder(root.left), self.preorder(root.right)
    def preorder(self, root):
        return [root.value] + self.preorder(root.left) + self.preorder(root.right) if root else []
            
    # def inorder(self, root):
    #     if root is not None:
    #         self.inorder(root.left), print(root.value), self.inorder(root.right)
    def inorder(self, root):
        return self.inorder(root.left) + [root.value] + self.inorder(root.right) if root else []
        
    # def postorder(self, root):
    #     if root is not None:
    #         self.postorder(root.left), self.postorder(root.right), print(root.value)
    def postorder(self, root):
        return self.postorder(root.left) + self.postorder(root.right) +  [root.value] if root else []
            
class BST(TreeNode):
    def Add(self, root, value):
        if root is None:
            self.root = Node(value)
        else:
            if value > root.value:
                if not root.right:
                    root.right = Node(value)
                else:
                    self.Add(root.right, value)
            elif value < root.value:
                if not root.left:
                    root.left = Node(value)
                else:
                    self.Add(root.left, value)
    
    def contains(self, node, value):
        if node is None:
            return False
        elif value == node.value:
            return True
        elif node.value < value:
            return self.contains(node.right, value)
        elif node.value > value:
            return self.contains(node.left, value)
        return False
    
    
tree1 = BST()
tree1.Add(None, 5)
tree1.Add(tree1.root, 4)
tree1.Add(tree1.root, 6)

print(tree1.preorder(tree1.root))
