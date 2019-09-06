class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not (l1 and l2):
            if l1 :
                return l1
            if l2:
                return l2
            return None

        if l1.val <= l2.val:
            start_result = ListNode(l1.val)
            l1 = l1.next
        else:
            start_result = ListNode(l2.val)
            l2 = l2.next
        result = start_result
        while(l1 and l2):
            if l1.val <= l2.val:
                result.next = ListNode(l1.val)
                l1 = l1.next
            else:
                result.next = ListNode(l2.val)
                l2 = l2.next
            result = result.next

        if l1:
            result.next = l1
        else:
            result.next = l2
        return start_result

def create_NodeList(l):
    start = ListNode(l[0])
    result = start
    if len(l) > 1:
        for i in l[1:]:
            result.next = ListNode(i)
            result = result.next
    return start

def show_NodeList(l):
    while(l.next):
        print(l.val, end=",")
        l = l.next
    print(l.val)

if __name__ == "__main__":
    l1 = create_NodeList([1,2,3])
    l2 = create_NodeList([1,3,4])
    s = Solution()
    show_NodeList(l1)
    show_NodeList(l2)
    show_NodeList(s.mergeTwoLists(l1,l2))
