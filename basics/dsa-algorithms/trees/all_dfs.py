class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


# Create nodes
A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

# Connect nodes
A.left = B
A.right = C

B.left = D
B.right = E

C.right = F   # <-- important correction

# Root
root = A

print(root)


def preOrder(node):
    if not node:
        return
    
    print(node)
    preOrder(node.left)
    preOrder(node.right)

# print(preOrder(A))

def inOrder(node):
    if not node:
        return
    
    inOrder(node.left)
    print(node)
    inOrder(node.right)

# print(inOrder(A))

def postOrder(node):
    if not node:
        return
    
    inOrder(node.left)
    inOrder(node.right)
    print(node)

# print(postOrder(A))

def preOrderIterative(node):
    stk = [node]
    
    while stk:
        node = stk.pop()
        print(node)
        if node.right:
            stk.append(node.right)
        if node.left:
            stk.append(node.left)

print(preOrderIterative(A))