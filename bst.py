class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.partent = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, new_val):
        if not self.root:
            self.root = Node(new_val)
            self.count += 1
        else:
            cursor = self.root
            while cursor != None:
                if new_val < cursor.val:
                    if cursor.left == None:
                        cursor.left = Node(new_val)
                        self.count += 1
                        return
                    else:
                        cursor = cursor.left
                if new_val > cursor.val:
                    if cursor.right == None:
                        cursor.right = Node(new_val)
                        self.count += 1
                        return
                    else:
                        cursor = cursor.right

    def search(self, search_val):
        cursor = self.root
        while cursor:
            if cursor.val == search_val:
                return cursor
            elif search_val < cursor.val:
                cursor = cursor.left
            else:
                cursor = cursor.right
        return None

    def get_in_order_traversal(self):
        def dfs(root, result):
            if not root:
                return
            dfs(root.left, result)
            result.append(root.val)
            dfs(root.right, result)

        result = []
        dfs(self.root, result)
        return result

    def rebalance(self):
        def build(values, lower, upper):
            size = upper - lower + 1
            if size <= 0:
                return
            middle = size // 2 + lower
            new_root = Node(values[middle])
            new_root.left = build(values, lower, middle - 1)
            new_root.right = build(values, middle + 1, upper)
            return new_root

        values = self.get_in_order_traversal()
        self.root = build(values, 0, len(values) - 1)

    def display(self):
        def dfs(root, result, level):
            if len(result) < level + 1:
                result.append([])
            if not root:
                # result[level].append(None)
                return

            dfs(root.left, result, level + 1)
            result[level].append(root.val)
            print(root.val, " ")
            dfs(root.right, result, level + 1)

        result = []
        dfs(self.root, result, 0)
        for line in result:
            print(line)
