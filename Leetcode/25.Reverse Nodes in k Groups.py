from NodeListsTools import *

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        start = ListNode(0)
        start.next = head
        last_gen = start
        next_gen = head

        while True:
            i = -1
            if not next_gen:
                last_gen.next = None
                break

            p = next_gen
            for i in range(k-1):
                
                if p.next:
                    p = p.next
                    continue
                else:
                    i = -1
                    break
            
            if i == k - 2:
                
                end = next_gen
                current = end
                post = current.next
                for j in range( k - 1 ):
                    past = current
                    current = post
                    post = current.next
                    current.next = past
                next_gen = post
                last_gen.next = current
                last_gen = end
            else:
                last_gen.next = next_gen

                break
                 
        return start.next
       
    def reverse(self, head: ListNode, k: int) -> ListNode:
        # count for linklist' Node
        count = 0
        if not head or not head.next  or k == 1:
            return head
        p = head
        while p:
            count += 1
            p = p.next
        # virtual Node
        v = ListNode(-999)
        v.next = None
        p, q, tail = v, head, head
        while k <= count:
            for i in range(k):
				# head insert
                if i == 0:
                    # save the last node
                    tail = q
                temp = q.next
                q.next = p.next
                p.next = q
                q = temp
            p = tail
            #p.next = None
            count -= k
        if count != 0:
            p.next = q
        return v.next

if __name__ == "__main__":
    s = Solution()
    l1 = create_NodeList([1,2,3,4,5,6])
    show_NodeList(s.reverse(l1, 3))

            


