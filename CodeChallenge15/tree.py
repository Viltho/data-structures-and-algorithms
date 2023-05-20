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
        """the preorder function is to arrange the values in the given tree at the given position in the tree based on root first then left then right

        Args:
            root (node): node is the root of the tree

        Returns:
            list: a list of preorder traversed nodes.
        """
        return [root.value] + self.preorder(root.left) + self.preorder(root.right) if root else []
            
    # def inorder(self, root):
    #     if root is not None:
    #         self.inorder(root.left), print(root.value), self.inorder(root.right)
    def inorder(self, root):
        """the inorder function is to arrange the values in the given tree at the given position in the tree based on left first then root then right

        Args:
            root (node): node is the root of the tree

        Returns:
            list: a list of inorder traversed nodes.
        """
        return self.inorder(root.left) + [root.value] + self.inorder(root.right) if root else []
        
    # def postorder(self, root):
    #     if root is not None:
    #         self.postorder(root.left), self.postorder(root.right), print(root.value)
    def postorder(self, root):
        """the postorder function is to arrange the values in the given tree at the given position in the tree based on left first then right then root

        Args:
            root (node): node is the root of the tree

        Returns:
            list: a list of postorder traversed nodes.
        """
        return self.postorder(root.left) + self.postorder(root.right) +  [root.value] if root else []
            
class BST(TreeNode):
    def Add(self, root, value):
        """adds a new node to the tree

        Args:
            root (node): base node reference to where the new node will be inserted
            value (number): is the value of the node
        """
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
        """search for a value in the tree

        Args:
            node (node): base node reference to where the search is performed
            value (number): is the value of the search

        Returns:
            Boolean: returns true if tree contains value, and false otherwise
        """
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
