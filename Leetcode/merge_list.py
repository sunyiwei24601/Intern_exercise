class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1: ListNode, l2: ListNode):
    start_node = ListNode(0)
    current_node = start_node
    
    while (l1 or l2):
        if  l2 == None:
            new_node = ListNode(l1.val)
            l1 = l1.next
        elif l1 == None:
            new_node = ListNode(l2.val)
            l2 = l2.next
        elif l1.val < l2.val:
            new_node = ListNode(l1.val)
            l1 = l1.next
        elif (l1 == None) or (l2.val <= l1.val) :
            new_node = ListNode(l2.val)
            l2 = l2.next
            
        current_node.next = new_node
        current_node = new_node
    return start_node.next


def create_Node_list(l):
    start_Node = ListNode(l[0])
    s_Node = start_Node
    for i in l[1:]:
        start_Node.next = ListNode(i)
        start_Node = start_Node.next
    return s_Node

def show_Node_list(l):
    c = l
    while (c):
        print(c.val, end = ' ')
        c = c.next
    print()

def reverse_track(head):
    if not head:
        return None,None
    
    new_node = ListNode(head.val)
    print(new_node.val)
    previous_node, start_node = reverse_track(head.next)
    if not previous_node:
        return new_node, new_node
    else:
        previous_node.next = new_node
        return new_node,start_node

a = create_Node_list([1,2,3])
new_node, start_node = reverse_track(a)
show_Node_list(start_node)





