from collections import deque

class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left, self.right = None, None

class BST:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def insert(self, val):
        self.root = self.insertHelper(val, self.root)
    def insertHelper(self, value, node):
        if node == None:
            node = TreeNode(value)
            return node

        # left
        if node.value > value:
            node.left = self.insertHelper(value, node.left)
        if node.value < value:
            node.right = self.insertHelper(value, node.right)

        return node

    def display(self):
        self.displayHelper(self.root, "Root Node: ")
    def displayHelper(self, node, details):
        if node == None:
            return

        print(details, node.value)

        self.displayHelper(node.left, "Left child of " + str(node.value) + " : ")
        self.displayHelper(node.right, "Right child of " + str(node.value) + " : ")


    def populate(self, nums):
        for num in nums:
            self.insert(num)

    def populateWithSorted(self, nums):
        self.populateWithSortedHelper(nums, 0, len(nums))
    def populateWithSortedHelper(self, nums, start, end):
        if start >= end:
            return
        mid = (start + end) // 2
        self.insert(nums[mid])

        self.populateWithSortedHelper(nums, start, mid)
        self.populateWithSortedHelper(nums, mid+1, end)

    def height(self):
        return self.heightHelper(self.root)
    def heightHelper(self, node):
        if node == None:
            return 0
        return 1 + max(self.heightHelper(node.left), self.heightHelper(node.right))

    def balanced(self):
        left = self.heightHelper(self.root.left)
        right = self.heightHelper(self.root.right)
        return abs(left - right) <= 1

    # BFS
    def bfs(self):
        if self.isEmpty():
            return

        queue = deque()
        queue.append(self.root)

        while queue:
             # level size
             ls = len(queue)

             for _ in range(ls):
                 popped = queue.popleft()
                 print(popped.value, end=" ")

                 if popped.left:
                     queue.append(popped.left)
                 if popped.right:
                     queue.append(popped.right)

             # newline
             print()

    # ZIGZAG
    def zigzag(self):
        ans = []

        if self.isEmpty():
            return ans

        queue = deque()
        queue.append(self.root)

        # Left to right variable
        ltr = True
        while queue:
             # level size
             ls = len(queue)

             # current level
             current = deque()

             for _ in range(ls):
                 popped = queue.popleft()

                 if ltr:
                     current.append(popped.value)
                 else:
                     current.appendleft(popped.value)

                 if popped.left:
                     queue.append(popped.left)
                 if popped.right:
                     queue.append(popped.right)

             # newline
             ans.append(list(current))
             ltr = not ltr
        return ans




if __name__ == '__main__':
    bst = BST()
    # bst.insert(15)
    # bst.insert(10)
    # bst.insert(30)
    # bst.insert(14)
    # bst.insert(25)
    bst.populate([15, 10, 30, 14, 25, 40])
    bst.bfs()

    print('\nZIGZAG')

    ans = bst.zigzag()
    for li in ans:
        print(li)
