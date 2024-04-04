class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Teste unitário
def test_reverseLinkedList():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    reversed_head = reverseLinkedList(head)
    assert reversed_head.val == 4
    assert reversed_head.next.val == 3
    assert reversed_head.next.next.val == 2
    assert reversed_head.next.next.next.val == 1

test_reverseLinkedList()
