from NodeListsTools import *

class Solution:
    def mergeKLists(self, lists):
        result_lists = []
        current_lists = lists[:]

        while(len(current_lists) > 1):
            lenth = len(current_lists)
            i = 0
            while( i < lenth - 1):
                result_lists.append(self.mergeTwoLists(current_lists[i], current_lists[i+1]) )
                i = i + 2
            if (i < lenth ):
                result_lists.append(current_lists[-1])
            current_lists = result_lists[:]
            result_lists = []
            show_NodeLists(current_lists)
            
        
        return current_lists


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

if __name__ == "__main__":
    s = Solution()
    l1 = create_NodeList([1,4,5])
    l2 = create_NodeList([1,3,4])
    l3 = create_NodeList([2,6])
    lists = [l1,l2,l3]
    show_NodeLists(s.mergeKLists(lists))