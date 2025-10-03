from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = tail = None

        while list1 and list2:
            if list1.val < list2.val:
                node = ListNode(list1.val, None)
                list1 = list1.next
            else:
                node = ListNode(list2.val, None)
                list2 = list2.next

            if head is None:
                head = tail = node
            else:
                tail.next = node
                tail = node

        if list1:
            if head is None:
                head = list1
            else:
                tail.next = list1
        elif list2:
            if head is None:
                head = list2
            else:
                tail.next = list2

        return head

def print_list(node: Optional[ListNode]):
    while node:
        print(node.val, end=' ')
        node = node.next
    print()


result = Solution().mergeTwoLists(None,
                        ListNode(1, ListNode(3, ListNode(4))))


print_list(result)