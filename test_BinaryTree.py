from unittest import TestCase
import BinaryTree


class TestTree(TestCase):
    def setUp(self) -> None:
        self.mock_tree = BinaryTree.Tree()
        self.mock_tree.insert(2)
        self.mock_tree.insert(6)
        self.mock_tree.insert(0)
        self.mock_tree.insert(7)
        self.mock_tree.insert(5)

    def test_find(self):
        self.assertEqual(True, self.mock_tree.find(2))
        self.assertEqual(False, self.mock_tree.find(4))

    def test_print(self):
        expected = [0, 2, 5, 6, 7]
        self.assertEqual(expected, self.mock_tree.printTree())

    def test_left_print(self):
        expected = [0]
        self.assertEqual(expected, self.mock_tree.printLeftTree())

    def test_right_print(self):
        expected = [6, 5, 7]
        self.assertEqual(expected, self.mock_tree.printRightTree())

    def test_average(self):
        self.assertEqual(4, self.mock_tree.averageTree())
        self.mock_tree.insert(4)
        self.assertEqual(4, self.mock_tree.averageTree())

        # Quick check
        expected = [0, 2, 4, 5, 6, 7]
        self.assertEqual(expected, self.mock_tree.printTree())

    def test_maximum_depth(self):
        self.assertEqual(3, self.mock_tree.maximum_depth())

    def test_graphicalPrintTree(self):
        expected = {2: [0, 6], 6: [5, 7]}
        self.assertEqual(expected, self.mock_tree.graphicalPrintTree())

    def test_shortest_dist(self):
        self.assertEqual(2, self.mock_tree.shortest_dist([5]))
        self.assertEqual(3, self.mock_tree.shortest_dist([5, 7]))
        self.assertEqual(2, self.mock_tree.shortest_dist([6, 7]))

    def test_remove(self):
        self.assertEqual(-1, self.mock_tree.remove(1))

        # removal
        self.mock_tree.remove(2)
        expected = [0, 5, 6, 7]
        self.assertEqual(expected, self.mock_tree.printTree())
        self.assertEqual(4.5, self.mock_tree.averageTree())

