class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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


def print_linked_list(head):
    """打印链表"""
    arr = linked_list_to_array(head)
    print(" -> ".join(map(str, arr)) if arr else "Empty list")


def linked_list_to_array(head):
    """将链表转换为数组用于验证"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result
