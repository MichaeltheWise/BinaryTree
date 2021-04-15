# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 2021

@author: Michael Lin
"""
import collections


class Node(dict):
    def __init__(self, val):
        super(Node, self).__init__()
        self.__dict__ = self
        self.left = None
        self.right = None
        self.val = val


class Tree(dict):
    def __init__(self):
        super(Tree, self).__init__()
        self.__dict__ = self
        self.root = None
        self.sum = 0
        self.count = 0

    def __contains__(self, key):
        return self.find(key)

    def __call__(self):
        print(self.printTree())

    def __len__(self):
        return len(self.printTree())

    def insert(self, num):
        """
        Binary tree insertion
        :param num: number to be inserted
        :return: None
        """
        if self.root is None:
            self.root = Node(num)
        else:
            if self.find(num):
                return
            else:
                # If the number exists, we don't need to insert
                self._insert_num(self.root, num)

    def _insert_num(self, node, num):
        """
        Implementation of insertion
        :param node: node
        :param num: number to be inserted
        :return: None
        """
        if num < node.val:
            if node.left is not None:
                self._insert_num(node.left, num)
            else:
                node.left = Node(num)
        else:
            if node.right is not None:
                self._insert_num(node.right, num)
            else:
                node.right = Node(num)

    def remove(self, num):
        """
        Binary tree removal
        :param num: number to be removed
        :return: None else -1 if not found
        """
        if self.root is None:
            return
        else:
            if self.find(num):
                # If the number exists, then we can remove it from the tree
                self._remove_num(self.root, num)
            else:
                return -1

    def _remove_num(self, node, num):
        """
        Implementation of removal
        :param node: node
        :param num: number to be removed
        :return: None
        """
        if node.val > num:
            node.left = self._remove_num(node.left, num)
        elif node.val < num:
            node.right = self._remove_num(node.right, num)
        else:
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right

            temp = self.minValNode(node.right)
            node.val = temp.val
            node.right = self._remove_num(node.right, temp.val)
        return node

    def minValNode(self, node):
        """
        Cases where both child exists, need to find the minimum val node by going down the left child of left tree
        :param node: node
        :return: return minimum value node
        """
        curr = node
        # This is for cases where both child nodes exist
        while curr.left is not None:
            curr = curr.left
        return curr

    def find(self, num):
        """
        Binary tree search
        :param num: desired number
        :return: Boolean True/False or None
        """
        if self.root is not None:
            return self._find(self.root, num)
        else:
            return None

    def _find(self, node, num):
        """
        Implementation of search
        :param node: node
        :param num: desired number
        :return: Boolean True/False
        """
        if node.val == num:
            return True
        elif num < node.val and node.left is not None:
            return self._find(node.left, num)
        elif num > node.val and node.right is not None:
            return self._find(node.right, num)
        else:
            return False

    def printTree(self):
        """
        Binary Tree Presentation
        :return: List of tree values
        """
        if self.root is not None:
            return self._print_Tree(self.root, res=[])

    def _print_Tree(self, node, res=[]):
        """
        Implementation of inorder traversal printing
        :param node: node
        :return: List of tree values
        """
        if node is not None:
            self._print_Tree(node.left, res)
            res.append(node.val)
            self._print_Tree(node.right, res)
            return res

    def averageTree(self):
        """
        Binary Tree Average Value Calculation
        :return: Average value
        """
        if self.root is not None:
            self.sum = 0
            self.count = 0
            self._average_Tree(self.root)
            return self.sum / self.count

    def _average_Tree(self, node):
        """
        Implementation of average value calculation
        :param node: node
        :return: Average value
        """
        if node is not None:
            self._average_Tree(node.left)
            self.sum += node.val
            self.count += 1
            self._average_Tree(node.right)

    def printLeftTree(self):
        """
        Binary Tree Left Tree Presentation
        :return: List of left subtree values
        """
        if self.root is not None:
            max_level = 0
            return self._print_Left_Tree(self.root.left, 1, max_level)

    def _print_Left_Tree(self, node, level, max_level, res=[]):
        """
        Implementation of left tree presentation
        :param node: node
        :param level: level
        :param max_level: maximum level
        :return: List of left subtree values
        """
        if node is None:
            return

        if max_level < level:
            res.append(node.val)
            max_level = level

        self._print_Left_Tree(node.left, level + 1, max_level, res)
        self._print_Left_Tree(node.right, level + 1, max_level, res)
        return res

    def printRightTree(self):
        """
        Binary Tree Right Tree Presentation
        :return: List of right subtree values
        """
        if self.root is not None:
            max_level = 0
            return self._print_Right_Tree(self.root.right, 1, max_level)

    def _print_Right_Tree(self, node, level, max_level, res=[]):
        """
        Implementation of right tree presentation
        :param node: node
        :param level: level
        :param max_level: maximum level
        :return: List of right subtree values
        """
        if node is None:
            return

        if max_level < level:
            res.append(node.val)
            max_level = level

        self._print_Right_Tree(node.left, level + 1, max_level, res)
        self._print_Right_Tree(node.right, level + 1, max_level, res)
        return res

    # Extension: more functions for fun
    def maximum_depth(self):
        """
        Binary Tree Maximum Depth Calculation
        :return: maximum depth of the binary tree
        """
        if self.root is None:
            return 0
        maximum_dist, stack = 0, [(self.root, 1)]
        while stack:
            node, dist = stack.pop(0)
            if dist > maximum_dist:
                maximum_dist = dist
            for child in [node.left, node.right]:
                if child is not None:
                    stack.append((child, dist + 1))
        return maximum_dist

    def shortest_dist(self, desired_list):
        """
        Binary Tree Minimum Distance From Root to Retrieve Nodes in Desired List
        :param desired_list: nodes in desired list
        :return: Minimum distance to retrieve those nodes
        """
        graph = self.graphicalPrintTree()
        # Walk through the graph from the lower leaves
        # Work the way up and collect any node that are in the extraction list
        dist_map = collections.defaultdict(int)
        for key in reversed(graph.keys()):
            for node in graph[key]:
                if node in dist_map.keys():
                    dist_map[key] = dist_map[node] + 1
                elif node in desired_list:
                    dist_map[key] += 1
        return dist_map[self.root.val]

    def graphicalPrintTree(self):
        """
        Graphical Representation of Binary Tree
        :return: Graphs with format {parent: [child, child...]}
        """
        graph = collections.defaultdict(list)
        if self.root is not None:
            stack = [self.root]
            # Graph generation into format {parent: [child, child...]}
            while stack:
                curr = stack.pop(0)
                for child in [curr.left, curr.right]:
                    if child is not None:
                        graph[curr.val].append(child.val)
                        stack.append(child)
        return graph


def main():
    # Testing before test is added
    tree = Tree()
    tree.insert(0)
    tree.insert(6)
    tree.insert(2)
    tree.insert(7)
    tree.insert(5)
    print("FIRST ROUND")
    print(tree.printTree())
    print("AVERAGE FIRST ROUND")
    print(tree.averageTree())
    tree.remove(3)
    tree.remove(6)
    print("SECOND ROUND")
    print(tree.printTree())
    print("AVERAGE SECOND ROUND")
    print(tree.averageTree())
    print("PRINT LEFT TREE")
    print(tree.printLeftTree())
    print("PRINT RIGHT TREE")
    print(tree.printRightTree())
    print("PRINT MINIMUM DISTANCE FROM 5 AND 7")
    print(tree.shortest_dist([5, 7]))

    # Dunder Method Test
    print("\nTEST OUT CONTAIN")
    print(6 in tree)
    print(3 in tree)
    print(2 in tree)
    print("TEST OUT CALL")
    tree()
    print("TEST OUT LENGTH")
    print(len(tree))


if __name__ == '__main__':
    main()
