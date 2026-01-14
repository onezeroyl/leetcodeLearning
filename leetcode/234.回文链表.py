# Definition for singly-linked list.
from typing import Optional
from list_common import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list = []
        while head:
            list.append(head.val)
            head = head.next

        list_reverse = list.copy()
        list.reverse()
        return list == list_reverse


if __name__ == "__main__":
    list_head = create_linked_list([1, 2, 2, 1])
    solution = Solution()
    print(solution.isPalindrome(list_head))
