class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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

def show_NodeLists(lists):
    for i in lists:
        show_NodeList(i)
