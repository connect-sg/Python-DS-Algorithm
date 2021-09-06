class Node:

    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.right_node = None
        self.left_node = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # we have to go to the left subtree
        if data < node.data:
            if node.left_node:
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)
        # we have to visit the right subtree
        else:
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)

    

    def get_predecessor(self, node):
        if node.right_node:
            return self.get_predecessor(node.right_node)

        return node

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):

        if node.left_node:
            self.traverse_in_order(node.left_node)

        print(node.data)

        if node.right_node:
            self.traverse_in_order(node.right_node)
    def depth(self):
        if self.root is None:
           return 0
        else:
           val = self.maxdepth(self.root,0)
           return val
            
    def maxdepth(self,node,n):
          if node is None:
              return n
          
           
          return max(self.maxdepth(node.left_node,n+1),self.maxdepth(node.right_node,n+1))
          
          
              


if __name__ == '__main__':

    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(6)
    bst.insert(1)
    bst.insert(7)

    print(bst.depth())
    print(bst.maxdepth(bst.root,0))
    #bst.traverse()
