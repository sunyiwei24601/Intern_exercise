from NodeListsTools import *
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        start = ListNode(0)
        start.next = head
        current_node = start
        while(current_node.next and current_node.next.next):
            left_node = current_node.next
            current_node.next = left_node.next
            current_node = current_node.next
            right_node = current_node.next
            current_node.next = left_node
            left_node.next = right_node
            current_node = current_node.next
        return start.next

if __name__ == "__main__":
    s = Solution()
    l1 = create_NodeList([1,2,3,4])
    show_NodeList(s.swapPairs(l1))
