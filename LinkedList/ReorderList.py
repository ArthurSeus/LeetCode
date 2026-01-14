from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next

        i = 0
        middle = (size // 2) -1
        curr = head
        otherList = None         
        while (i <= middle):
            if i == middle:
                otherList = curr.next
                curr.next = None
                break
            curr = curr.next
            i += 1

        curr = otherList
        next_node = curr.next
        curr.next = None
        while curr and next_node:
            tmp = next_node.next
            next_node.next = curr
            curr = next_node
            next_node = tmp
        
        list1 = head.next
        list2 = curr
        res = head
        alternate = True
        while list1 and list2:
            if alternate:
                res.next = list2
                list2 = list2.next
                alternate = False
            else:
                res.next = list1
                list1 = list1.next
                alternate = True
            
            res = res.next
        
        if list1:
            res.next = list1
        elif list2:
            res.next = list2

        return head


# ---------- helpers for local testing ----------

def build_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def list_to_array(head: Optional[ListNode]) -> List[int]:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


def run_tests():
    s = Solution()

    # Example 1
    head = build_list([2, 4, 6, 8])
    s.reorderList(head)
    print("Output:", list_to_array(head))  # expected [2, 8, 4, 6]

    print("-" * 40)

    # Example 2
    head = build_list([2, 4, 6, 8, 10])
    s.reorderList(head)
    print("Output:", list_to_array(head))  # expected [2, 10, 4, 8, 6]


if __name__ == "__main__":
    run_tests()
