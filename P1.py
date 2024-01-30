#Problem 1:
n, Q = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if A[i] + A[j] >= Q:
            cnt += 1
print(cnt) 


# problem 2:

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, curr, value):
        if curr == None:
            return Node(value)
        
        if value < curr:
            curr.left = self.insert(curr.left, value)
        elif value > curr:
            curr.right = self.insert(curr.right, value)
        
        return curr
    
    def dfs(self, curr):
        if curr == None:
            return 0, 0
        if curr.left == None and curr.right == None:
            return 1, 0
        
        cr, rr = self.dfs(curr.right)
        cl, rl = self.dfs(curr.left)

        count = cr + cl + 1
        res = rr + rl
        
        if cr == cl:
            res += 1

        return count, res
    
n = input()
A = list(map(int, input().split()))

bst = BST()

for an in A:
    bst.root = bst.insert(bst.root, an)

count, res = bst.dfs(bst.root)

print(count)

