

# 1 -> 2 -> 3 -> 4
# 4 -> 3 -> 2 -> 1
def reverse_list_recursion(self, head):
    if not head or not head.next:
        return head

    prev = self.reverse_list_recursion(head.next)
    head.next.next = head
    head.next = None
    return prev


def reverse_list(self, head):
    prev_node = next_node = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev_node
        prev_node = curr
        curr = next_node

    return prev_node


