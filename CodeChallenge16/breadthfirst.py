import time
from CodeChallenge10.queue import Queue

class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value
        
class TreeNode:
    def __init__(self):
        self.root = None
        self.max = 0
        self.queue = Queue()
        
    def getMaxone(self, root):
        if root:
            if root.value > self.max:
                self.max = root.value
            self.getMaxone(root.right)
            self.getMaxone(root.left)
        return self.max
    
    def getMaxtwo(self):
        self.max = self.queue.front.value
        while self.queue.front:
            if self.queue.front.value > self.max:
                self.max = self.queue.front.value
            else:
                self.queue.front = self.queue.front.next
        return self.max
    
    def getMax(self):
        queue = self.bfs(self.root)
        if not queue:
            return self.max
        self.max = queue[0]
        for i in queue:
            if i > self.max:
                self.max = i
        return self.max
            
    def bfs(self, node):
        queue = Queue()
        returned_list = []
        if node is None:
            return []
        queue.enqueue(node)
        while queue.front:
            node = queue.dequeue()
            returned_list.append(node.value)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return returned_list

    def add(self, value):
        self.queue.enqueue(value)
        
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
        
tree1 = TreeNode()
node1 = Node(1)
node2 = Node(5)
node3 = Node(4)
node4 = Node(2)
node5 = Node(6)
node6 = Node(3)
node7 = Node(9)

tree1.root = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

print(tree1.getMax())
