class TreeNode:

    def __init__(self, left, label, right):
        self.left = left
        self.label = label
        self.right = right

    def is_leaf(self):
        return self.left == None and self.right == None

    def __str__(self):
        def viz_helper(node, indent):
            result = ""
            if node == None:
                return result
            result = result + str(node.label) + "\n"
            if node.left != None:
                left_str = viz_helper(node.left, indent+2)
                result = result + (" " * indent) + "--L--> " + left_str
            if node.right != None:
                right_str = viz_helper(node.right, indent+2)
                result = result + (" " * indent) + "--R--> " + right_str
            return result
        return viz_helper(self, 0).strip()

