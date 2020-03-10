# Vladislav Saburov
# Project 1 435
import random


class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.value = value
        # Added for AVL Tree
        self.parent = None
        self.height = 1
        self.balance_factor = 0


class BSTTree:
    # Initializes the BSTTree to have no root
    def __init__(self):
        self.root = None
        # Question 6a
        self.count = 0

    """ ============================================================================================= """
    """ =================================== RECURSIVE =============================================== """
    """ ============================================================================================= """

    # Checks if the root is None, if it is creates a node with that value
    def insertRec(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insertRec(self.root, value)

    # If the node is none creates the Node(value)
    # if the value is less than the node value, insert is called on the left child
    # If the value is greater node belongs on right side
    def _insertRec(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left_child = self._insertRec(node.left_child, value)
        elif value >= node.value:
            node.right_child = self._insertRec(node.right_child, value)
        return node

    # Checks if the root is None, if is is just returns else runs helper
    def deleteRec(self, value):
        if self.root is None:
            return
        else:
            self._deleteRec(self.root, value)

    # If the node is none returns, traverses tree until node is found
    # if the node has no child just remove, if it has one child it is then replaced by its child
    # if the node has both children then when removed it is replaced by the min value in is right subtree
    def _deleteRec(self, node, value):
        if node is None:
            return
        if value > node.value:
            node.right_child = self._deleteRec(node.right_child, value)
        elif value < node.value:
            node.left_child = self._deleteRec(node.left_child, value)
        else:
            if node.right_child is None and node.left_child is None:
                node = None
            elif node.left_child is None:
                node = node.right_child
            elif node.right_child is None:
                node = node.left_child
            else:
                value = self._findMinRec(node.right_child)
                node.value = value
                node.right_child = self._deleteRec(node.right_child, value)
        return node

    # Checks if root is none, if it is return, else run helper
    def findNextRec(self, value):
        if self.root is None:
            return
        else:
            return self._findNextRec(self.root, value)

    # Find the next biggest value, inorder-successor. Once value is found go one step right then traverse the left tree
    # which is done by the findMin function can also use the inorderTraversal function and use that
    # array to find
    def _findNextRec(self, node, value, nex=None):
        if node is None:
            return
        if node.value == value:
            if node.right_child:
                return self._findMinRec(node.right_child)
        elif value < node.value:
            nex = node
            return self._findNextRec(node.left_child, value, nex)
        else:
            return self._findNextRec(node.right_child, value, nex)
        if nex is None:
            return
        else:
            return nex.value

    # Checks if root is none, if it is return, else run helper
    def findPrevRec(self, value):
        if self.root is None:
            return
        else:
            return self._findPrevRec(self.root, value)

    # Find the smaller value, inorder-predecessor.Once value is found go one step left then traverse the right tree for
    # the biggest left which is done by the findMin function can also use the inorderTraversal function and use that
    # array to find
    def _findPrevRec(self, node, value, prev=None):
        if node is None:
            return
        if node.value == value:
            if node.left_child:
                return self._findMaxRec(node.left_child)
        elif value < node.value:
            return self._findPrevRec(node.left_child, value, prev)
        else:
            prev = node
            return self._findPrevRec(node.right_child, value, prev)
        if prev is None:
            return
        else:
            return prev.value

    # if root is none return, else run helper
    def findMinRec(self):
        if self.root is None:
            return
        else:
            return self._findMinRec(self.root)

    # While there is a left child, traverse the left tree
    def _findMinRec(self, node):
        while node.left_child:
            return self._findMinRec(node.left_child)
        return node.value

    # if root is none return, else run helper
    def findMaxRec(self):
        if self.root is None:
            return
        else:
            return self._findMaxRec(self.root)

    # If right child exists, traverse the right tree
    def _findMaxRec(self, node):
        while node.right_child:
            return self._findMaxRec(node.right_child)
        return node.value

    # If root is none, return else run helper
    def inOrderRec(self):
        if self.root is None:
            return
        else:
            return self._inOrderRec(self.root)

    # If the node is not empty append onto a list the inOrder traversal
    def _inOrderRec(self, node, node_list=[]):
        if node:
            self._inOrderRec(node.left_child, node_list)
            node_list.append(node.value)
            self._inOrderRec(node.right_child, node_list)
        return node_list

    """ ============================================================================================= """
    """ ================================= ITERATIVE ================================================= """
    """ ============================================================================================= """

    # If the root is none, create a Node. While the node is not None, check if value is bigger or smaller than the
    # current node.value and insert a node into that nodes child. If child exists, than traverse until empty spot found
    def insertIter(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            node = self.root
            while node:
                # Question 6a
                self.count += 1
                if value < node.value:
                    if node.left_child is None:
                        node.left_child = Node(value)
                        break
                    else:
                        node = node.left_child
                elif value >= node.value:
                    if node.right_child is None:
                        node.right_child = Node(value)
                        break
                    else:
                        node = node.right_child

    # If the root is none return. While the value of the node is not the value, traverse tree until the node is found
    # and store the previous node (parent). If the node is not null check to see the children of the node that is to be
    # deleted. If no children then check what side of the parent this node was one and set it to None, if one child then
    # check which side of parent and set it to the nodes remaining child. If two children then find the minimum value
    # in the right tree (successor) and set it to the node. Then move that node to be the parent maintaining its tree
    def deleteIter(self, value):
        if self.root is None:
            return
        else:
            node = self.root
            while node.value != value:
                # Question 6a
                self.count += 1
                prev_node = node
                if value > node.value:
                    node = node.right_child
                elif value < node.value:
                    node = node.left_child
            while node:
                if node.right_child is None and node.left_child is None:
                    if value < prev_node.value:
                        prev_node.left_child = None
                        break
                    else:
                        prev_node.right_child = None
                        break
                elif node.left_child is None:
                    if value < prev_node.value:
                        prev_node.left_child = node.right_child
                        break
                    else:
                        prev_node.right_child = node.right_child
                        break
                elif node.right_child is None:
                    if value < prev_node.value:
                        prev_node.left_child = node.left_child
                        break
                    else:
                        prev_node.right_child = node.left_child
                        break
                else:
                    value = self._findMinIter(node.right_child)
                    node.value = value
                    prev_node = node
                    node = node.right_child

    # Get the inorder list of the tree if the value exists then find the index of the value, and then get the next index
    def findNextIter(self, value):
        node_list = self.inOrderIter()
        if value in node_list:
            value_index = node_list.index(value)
            if value_index == len(node_list) - 1:
                return
            else:
                return node_list[value_index + 1]

    # Get the inorder list of the tree if the value exists then find the index of the value, and then get the prev index
    def findPrevIter(self, value):
        node_list = self.inOrderIter()
        if value in node_list:
            value_index = node_list.index(value)
            if value_index == 0:
                return
            else:
                return node_list[value_index - 1]

    # If the root is not none, then while there is a left child traverse the left
    def findMinIter(self):
        if self.root is None:
            return
        else:
            node = self.root
            while node.left_child:
                # Question 6a
                self.count += 1
                node = node.left_child
            return node.value

    # Helper find min that takes in a distinct node and traverses that nodes subtree
    def _findMinIter(self, node):
        while node.left_child:
            # Question 6a
            self.count += 1
            node = node.left_child
        return node.value

    # if the root is not none, then while there is right child traverse the right
    def findMaxIter(self):
        if self.root is None:
            return
        else:
            node = self.root
            while node.right_child:
                # Question 6a
                self.count += 1
                node = node.right_child
            return node.value

    # create a stack that adds the visited nodes, when no more nodes and stack is not empty then append the current node
    # to the node list
    def inOrderIter(self):
        if self.root is None:
            return
        else:
            node_list = []
            stack = []
            current_node = self.root
            while True:
                if current_node:
                    # Question 6a
                    self.count += 1
                    stack.append(current_node)
                    current_node = current_node.left_child
                else:
                    if not stack:
                        break
                    else:
                        current_node = stack.pop()
                        node_list.append(current_node.value)
                        current_node = current_node.right_child

            return node_list


class AVLTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def insertIter(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            node = self.root
            while node:
                self.count += 1
                if value < node.value:
                    if node.left is None:
                        node.left = Node(value)
                        node.left.parent = node
                        self.balance(node)
                        break
                    else:
                        node = node.left
                elif value >= node.value:
                    if node.right is None:
                        node.right = Node(value)
                        node.right.parent = node
                        self.balance(node)
                        break
                    else:
                        node = node.right

    def deleteIter(self, value):
        if self.root is None:
            return
        else:
            node = self.root
            while node.value != value:
                # Question 6a
                self.count += 1
                prev_node = node
                if value > node.value:
                    node = node.right_child
                elif value < node.value:
                    node = node.left_child
            while node:
                if node.right_child is None and node.left_child is None:
                    if value < prev_node.value:
                        prev_node.left_child = None
                        self.balance(prev_node)
                        break
                    else:
                        prev_node.right_child = None
                        self.balance(prev_node)
                        break
                elif node.left_child is None:
                    if value < prev_node.value:
                        prev_node.left_child = node.right_child
                        self.balance(prev_node)
                        break
                    else:
                        prev_node.right_child = node.right_child
                        self.balance(prev_node)
                        break
                elif node.right_child is None:
                    if value < prev_node.value:
                        prev_node.left_child = node.left_child
                        self.balance(prev_node)
                        break
                    else:
                        prev_node.right_child = node.left_child
                        self.balance(prev_node)
                        break
                else:
                    value = self._findMinIter(node.right_child)
                    node.value = value
                    prev_node = node
                    node = node.right_child
                    self.balance(node)

    def balance(self, node):
        self.setHeight()
        self.setBalanceFactor()
        if node.parent:
            while abs(node.parent.balance_factor) > 1:
                if node.parent.balance_factor > 1:
                    self.rightRotate(node)
                    self.setHeight()
                    self.setBalanceFactor()
                else:
                    self.leftRotate(node)
                    self.rightRotate(node)
                    self.setHeight()
                    self.setBalanceFactor()
                if node.parent.balance_factor < -1:
                    self.leftRotate(node)
                    self.setHeight()
                    self.setBalanceFactor()
                else:
                    self.rightRotate(node)
                    self.leftRotate(node)
                    self.setHeight()
                    self.setBalanceFactor()

    # goes through tree and sets the balance factor of each node
    def setBalanceFactor(self):
        node_list = self.inOrderIter()
        for node in node_list:
            node.balance_factor = self.getHeight(node.left) - self.getHeight(node.right)

    def getHeight(self, node):
        if node:
            return node.height
        else:
            return -1

    # goes through tree and sets the height of each node
    def setHeight(self):
        node_list = self.inOrderIter()
        for node in node_list:
            node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

    # Cant get rotations to work right
    def leftRotate(self, node):
        old_root = node.parent
        old_root_parent = node.parent.parent
        node.left = old_root
        node.parent = old_root_parent

    def rightRotate(self, node):
        old_root = node.parent
        old_root_parent = node.parent.parent
        node.right = old_root
        node.parent = old_root_parent

    # Get the inorder list of the tree if the value exists then find the index of the value, and then get the next index
    def findNextIter(self, value):
        node_list = self.inOrderIter()
        if value in node_list:
            value_index = node_list.index(value)
            if value_index == len(node_list) - 1:
                return
            else:
                return node_list[value_index + 1]

    # Get the inorder list of the tree if the value exists then find the index of the value, and then get the prev index
    def findPrevIter(self, value):
        node_list = self.inOrderIter()
        if value in node_list:
            value_index = node_list.index(value)
            if value_index == 0:
                return
            else:
                return node_list[value_index - 1]

    # If the root is not none, then while there is a left child traverse the left
    def findMinIter(self):
        if self.root is None:
            return
        else:
            node = self.root
            while node.left_child:
                # Question 6a
                self.count += 1
                node = node.left_child
            return node.value

    # Helper find min that takes in a distinct node and traverses that nodes subtree
    def _findMinIter(self, node):
        while node.left_child:
            # Question 6a
            self.count += 1
            node = node.left_child
        return node.value

    # if the root is not none, then while there is right child traverse the right
    def findMaxIter(self):
        if self.root is None:
            return
        else:
            node = self.root
            while node.right_child:
                # Question 6a
                self.count += 1
                node = node.right_child
            return node.value

    # create a stack that adds the visited nodes, when no more nodes and stack is not empty then append the current node
    # to the node list
    def inOrderIter(self):
        if self.root is None:
            return
        else:
            node_list = []
            stack = []
            current_node = self.root
            while True:
                if current_node:
                    # Question 6a
                    self.count += 1
                    stack.append(current_node)
                    current_node = current_node.left_child
                else:
                    if not stack:
                        break
                    else:
                        current_node = stack.pop()
                        node_list.append(current_node.value)
                        current_node = current_node.right_child

            return node_list


def getRandomArray(size):
    random_array = []
    for number in range(0, size):
        random_number = random.randint(0, size)
        while random_number in random_array:
            random_number = random.randint(0, size)
        random_array.append(random_number)
    return random_array


def getSortedArray(size):
    sorted_array = []
    for number in range(size, -1, -1):
        sorted_array.append(number)
    return sorted_array


def sort(unsorted_list):
    tree = BSTTree()
    for item in unsorted_list:
        tree.insertIter(item)
    sorted_list = tree.inOrderIter()
    return sorted_list


# Question 6B
random_bst = BSTTree()
random_array = getRandomArray(10000)
for number in random_array:
    random_bst.insertIter(number)

print("BST tree levels:", random_bst.count)

# Question 6C
sorted_bst = BSTTree()
sorted_array = getSortedArray(10000)
for number in sorted_array:
    sorted_bst.insertIter(number)

print("BST tree levels:", sorted_bst.count)
