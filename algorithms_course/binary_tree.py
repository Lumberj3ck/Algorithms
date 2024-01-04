# 100 200 50 10 22 44 77
# Graph traversal
# Breadth fisrt BFS
# travers all children nodes and then children of those children
# we put all the childre of current node to the queue
# Depth First DFS
# travers all children of first children
# we put all children of node to the stack and then next nodes children
# dijkstra algorithm
class TreeNode:
    def __init__(self, data, right_children=None, left_children=None):
        self.data = data
        self.right_children = None
        self.left_children = None


class Tree:
    def __init__(self, root: TreeNode):
        self.root = root


new_tree = Tree(root=TreeNode(15, right_children=TreeNode(139)))

