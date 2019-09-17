# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        def tail_and_length():
            node = head
            length = 0
            while node:
                length += 1
                if not node.next:
                    tail = node
                node = node.next
            return (tail, length)

        def rotate(head):
            node = head
            for i in range(length - k - 1):
                node = node.next
            next_node = node.next
            node.next = None
            tail.next = head
            head = next_node
            return head

        (tail, length) = tail_and_length()
        k %= length
        if k == 0:
            return head
        return rotate(head)
