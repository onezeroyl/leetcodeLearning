# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        node_list = []
        index = 0
        while head is not None:
            node_list.append(head)
            next_node = head.next
            if index != 0:
                node_list[index].next = node_list[index - 1]
            else:
                head.next = None
            head = next_node
            index += 1
        return node_list[index - 1]

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev


def create_linked_list(arr):
    """根据数组创建链表"""
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next

    return head


def linked_list_to_array(head):
    """将链表转换为数组用于验证"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def print_linked_list(head):
    """打印链表"""
    arr = linked_list_to_array(head)
    print(" -> ".join(map(str, arr)) if arr else "Empty list")


# 测试用例
if __name__ == "__main__":
    solution = Solution()

    # 测试用例1: [1,2,3,4,5] -> [5,4,3,2,1]
    print("测试用例1:")
    original1 = create_linked_list([1, 2, 3, 4, 5])
    print("原链表:", end=" ")
    print_linked_list(original1)
    reversed1 = solution.reverse_list(original1)
    print("反转后:", end=" ")
    print_linked_list(reversed1)
    print("验证结果:", linked_list_to_array(reversed1) == [5, 4, 3, 2, 1])
    print()

    # 测试用例2: [1,2] -> [2,1]
    print("测试用例2:")
    original2 = create_linked_list([1, 2])
    print("原链表:", end=" ")
    print_linked_list(original2)
    reversed2 = solution.reverse_list(original2)
    print("反转后:", end=" ")
    print_linked_list(reversed2)
    print("验证结果:", linked_list_to_array(reversed2) == [2, 1])
    print()

    # 测试用例3: [] -> []
    print("测试用例3:")
    original3 = create_linked_list([])
    print("原链表:", end=" ")
    print_linked_list(original3)
    reversed3 = solution.reverse_list(original3)
    print("反转后:", end=" ")
    print_linked_list(reversed3)
    print("验证结果:", linked_list_to_array(reversed3) == [])
    print()

    # 测试用例4: [1] -> [1]
    print("测试用例4:")
    original4 = create_linked_list([1])
    print("原链表:", end=" ")
    print_linked_list(original4)
    reversed4 = solution.reverse_list(original4)
    print("反转后:", end=" ")
    print_linked_list(reversed4)
    print("验证结果:", linked_list_to_array(reversed4) == [1])
