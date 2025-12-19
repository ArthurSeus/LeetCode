from typing import Optional, List

class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def addTwoNumbers(self,l1: Optional[ListNode],l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ""
        n2 = ""
        l1p = l1
        l2p = l2
        while l1p:
            n1 += str(l1p.val)
            l1p = l1p.next
        while l2p:
            n1 += str(l2p.val)
            l2p = l2p.next
        
        n1 = int(n1[::-1])
        n2 = int(n2[::-1])

        result = n1 + n2
        
        head = None
        curr = None
        for c in reversed(str(result)):
            node = ListNode(c)
            if not head:
                head = node
                curr = node
            else:
                curr.next = node
                curr = node
        
        return head
        pass


# ---------- Helpers ----------

def build_list(values: List[int]) -> Optional[ListNode]:
    head = None
    curr = None
    for v in values:
        node = ListNode(v)
        if not head:
            head = node
            curr = node
        else:
            curr.next = node
            curr = node
    return head


def list_to_array(node: Optional[ListNode]) -> List[int]:
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


# ---------- Execução local ----------

if __name__ == "__main__":
    l1 = build_list([2, 4, 3])
    l2 = build_list([5, 6, 4])

    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)

    print(list_to_array(result))
