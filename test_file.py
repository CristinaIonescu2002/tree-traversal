import unittest
from tree import Tree

class TestTreeFind(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        self.tree.add(5)
        self.tree.add(3)
        self.tree.add(7)
        self.tree.add(2)
        self.tree.add(4)
        self.tree.add(6)
        self.tree.add(8)

    def test_find_existing_node(self):
        found_node = self.tree._find(3, self.tree.root)
        self.assertIsNotNone(found_node, "Test 1 failed: Node not found.")
        self.assertEqual(found_node.data, 3, "Test 1 failed: Incorrect node found.")

    def test_find_non_existing_node(self):
        not_found_node = self.tree._find(10, self.tree.root)
        self.assertIsNone(not_found_node, "Test 2 failed: Found unexpected node.")

if __name__ == '__main__':
    unittest.main()