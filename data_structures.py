class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def set_val(self, new_val):
        self.val = new_val

    def set_next(self, new_next):
        self.next = new_next

    def get_val(self):
        return self.val

    def get_next(self):
        return self.next


class LinkedList:
    def __init__(self):
        # self.head = ListNode(val)
        # self.last = self.head
        self.head = None
        self.last = None

    def append(self, val):
        if self.head:
            self.last.next = ListNode(val)
            self.last = self.last.next
        else:
            self.head = ListNode(val)
            self.last = self.head

    def display(self):
        cursor = self.head
        output = "{ "
        while cursor:
            output += f"{str(cursor.get_val())}, "
            cursor = cursor.next
        output = output + " }"
        return output

    def size(self):
        size = 0
        cursor = self.head
        while cursor:
            size += 1
            cursor = cursor.next
        return size

    def search(self, search_val):
        cursor = self.head
        while cursor:
            if cursor.val == search_val:
                return True
            cursor = cursor.next
        return False

    def delete(self, delete_val):
        prev = None
        cursor = self.head
        while cursor:
            if cursor.get_val() == delete_val:
                if prev:  # if it's not first node
                    if cursor == self.last:  # change pointer on last node
                        prev.next = None
                        self.last = prev
                    else:
                        prev.next = cursor.next
                    return
                else:  # if it's first node
                    self.head = cursor.next
                    return
            prev = cursor
            cursor = cursor.next
        else:
            raise ValueError("No such value")

    def insert(self, index, val):
        size = self.size()
        if index > size:
            self.append(val)
        elif index == 1:
            tmp = self.head
            self.head = ListNode(val, tmp)
        else:
            cursor = self.head
            for _ in range(index - 2):
                cursor = cursor.next
            tmp = cursor.next
            cursor.next = ListNode(val, tmp)

    def __len__(self):
        return self.size()

    def __str__(self):
        return self.display()


class DoubleListNode:
    def __init__(self, val, next, prev) -> None:
        self.val = val
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, val):
        self.root = TreeNode(val)


class Stack:
    def __init__(self) -> None:
        self.stack = []

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def __str__(self) -> str:
        return " ".join([str(i) for i in self.stack])


a = [1,2,3,2,13,1,]